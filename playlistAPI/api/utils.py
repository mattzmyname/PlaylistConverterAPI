import uuid

from .models import songsByPlatform
from .serializers import SongByPlatformSerializer


def existsInSongPlatformModel(songID):
	try:
		query_output = songsByPlatform.objects.get(spotifyID=songID)
		return query_output
	except Exception as e:
		pass


def getOrCreateRelationship(songID, platform):
	query_output = existsInSongPlatformModel(songID)
	if query_output is not None:
		return query_output.songID

	new_SongID = uuid.uuid4()
	platform_relationship = SongByPlatformSerializer(data={
		platform.lower() + 'ID': songID,
		'songID': new_SongID
	})
	if platform_relationship.is_valid():
		platform_relationship.save()
	return new_SongID
