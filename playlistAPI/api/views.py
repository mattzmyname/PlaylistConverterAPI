from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data_api import spotify
from .serializers import *
from .utils import getOrCreateRelationship, queryByAppSongID, addSongDB


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
					song.appSong_id = getOrCreateRelationship(song.appSong_id, song.platform, song)
					song_data = vars(song)
					addSongDB(song_data)
					response_list.append(song_data)
				return Response({"Playlist Name": name, "Songs": response_list, "playlist_size": len(response_list)})
			except Exception as e:
				return Response({'error': str(e)}, status=500)
		else:
			return Response({"error": f"Platform {platform} not supported"})
	else:
		return Response({"error": "playlist url not found"})


def createPlaylist(postData, platform='spotify'):
	if 'username' not in postData:
		return Response({"error": f"Post requires 'username' key-value"})
	if 'Playlist Name' not in postData:
		return Response({"error": f"Post requires 'Playlist Name' key-value"})
	if 'Songs' not in postData:
		return Response({"error": f"Post requires 'Songs' key-value"})

	if platform.lower() == 'spotify':
		username = postData['username']
		client = spotify.Spotify(username)
		playlistName = postData['Playlist Name']
		songIDs = [queryByAppSongID(song['id'], platform) for song in postData['Songs']]
		if client.createPlaylist(name=playlistName, songList=songIDs):
			return Response({"message": f"Created playlist {playlistName} for {username}"})
		return Response({"error": f"Failed to create playlist {playlistName} for {username}"})
	else:
		return Response({"error": f"Platform {platform} not supported"})
