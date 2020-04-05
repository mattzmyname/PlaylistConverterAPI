from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *


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
def playlistParse(request):
	print(request)
	return hello_world(request)
