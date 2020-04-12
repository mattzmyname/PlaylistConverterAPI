from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data_api import spotify
from .serializers import *
from .utils import getOrCreateRelationship, queryByAppSongID


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


class SongsViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows songs to be viewed or edited.
	"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer


class SongByPlatformViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows songs_by_platform to be viewed or edited.
	"""
	queryset = songsByPlatform.objects.all()
	serializer_class = SongByPlatformSerializer


# Using regular view
@api_view()
def hello_world(request):
	return Response({"message": "Hello, world!"})


@api_view(['GET', 'POST'])
def playlist(request, platform=None):
	if request.method == 'GET':
		return readPlaylist(request, platform)
	else:  # this is a post now
		return createPlaylist(request.data, platform)


def readPlaylist(request, platform):
	if 'url' in request.query_params:
		if platform.lower() == 'spotify':
			playlistURL = request.query_params['url']
			client = spotify.Spotify()  # pass auth as env variable
			try:
				thisPlaylist = client.parsePlaylist(playlistURL)
				name = thisPlaylist.name
				songList = thisPlaylist.songs
				response_list = []
				for song in songList:
					song.id = getOrCreateRelationship(song.id, song.platform)
					serializer = SongSerializer(data=vars(song))
					if serializer.is_valid(raise_exception=False):
						serializer.save()
					response_list.append(serializer.data)
				return Response({"Playlist Name": name, "Songs": response_list, "playlist_size": len(response_list)})
			except Exception as e:
				return Response({'error': str(e)}, status=500)
		else:
			return Response({"error": f"Platform {platform} not supported"})
	else:
		return Response({"error": "playlist url not found"})


def createPlaylist(postData, platform='spotify'):
	if platform.lower() == 'spotify':
		username = 'mattzmyname'
		client = spotify.Spotify(username)
		songIDs = [queryByAppSongID(song['id'], platform) for song in postData['Songs']]
		client.createPlaylist(name=postData['Playlist Name'], songList=songIDs)
		return Response({"message": 12})

	else:
		return Response({"error": f"Platform {platform} not supported"})
