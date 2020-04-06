from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .data_api import spotify
from .serializers import *
from .utils import getOrCreateRelationship


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


@api_view(['GET'])
def playlistParse(request, platform=None):
	if 'url' in request.query_params and platform.lower() == 'spotify':
		playlist = request.query_params['url']
		client = spotify.Spotify()  # pass auth as env variable
		try:
			songList = client.parsePlaylist(playlist)
			response_list = []
			for song in songList:
				song.id = getOrCreateRelationship(song.id, song.platform)
				serializer = SongSerializer(data=vars(song))
				if serializer.is_valid(raise_exception=False):
					serializer.save()
				response_list.append(serializer.data)

			return Response({"Songs": response_list, "playlist_size": len(response_list)})
		except Exception as e:
			return Response({'error': str(e)}, status=500)
	return Response({"error": "playlist url not found"})
