import time
import uuid

from .models import songsByPlatform
from .serializers import SongByPlatformSerializer


def queryByAppSongID(appSongID, platform):
	try:
		query_output = songsByPlatform.objects.get(songID=appSongID)
		if platform == 'spotify':
			targetID = query_output.spotifyID
		elif platform == 'apple':
			targetID = query_output.appleID
		elif platform == 'youtube':
			targetID = query_output.youtubeID
		else:
			return
		return targetID if targetID != "" else lookupSong(appSongID, platform)
	except Exception as e:
		print("db error")
		pass


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


def lookupSong(appSongID, platform):  # todo
	pass


def timeit(method):
	def timed(*args, **kw):
		ts = time.time()
		result = method(*args, **kw)
		te = time.time()
		if 'log_time' in kw:
			name = kw.get('log_name', method.__name__.upper())
			kw['log_time'][name] = int((te - ts) * 1000)
		else:
			print('%r  %2.2f ms' % (method.__name__, (te - ts) * 1000))
		return result

	return timed
