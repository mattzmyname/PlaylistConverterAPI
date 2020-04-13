import time
import uuid

from .models import songsByPlatform, Song
from .serializers import SongByPlatformSerializer, SongSerializer


def queryByAppSongID(appSongID, platform):
	try:
		query_output = songsByPlatform.objects.get(songID=appSongID)
		targetID = findIDInQueryOutput(query_output, platform)
		return targetID if targetID != "" else lookupSong(appSongID, platform)
	except Exception as e:
		print("db error")
		pass


def updateSongPlatform(appSongID, platformSongID, platform):
	query_output = songsByPlatform.objects.get(songID=appSongID)
	if platform == 'spotify':
		query_output.spotifyID = platformSongID
	elif platform == 'apple':
		query_output.appleID = platformSongID
	elif platform == 'youtube':
		query_output.youtubeID = platformSongID


def existsInSongPlatformModel(songID, platform):
	try:
		if platform == 'spotify':
			query_output = songsByPlatform.objects.get(spotifyID=songID)
		elif platform == 'apple':
			query_output = songsByPlatform.objects.get(appleID=songID)
		elif platform == 'youtube':
			query_output = songsByPlatform.objects.get(youtubeID=songID)
		else:
			query_output = None
		return query_output
	except Exception as e:
		print(e)
		pass


def findIDInQueryOutput(query_output, platform):
	if platform == 'spotify':
		targetID = query_output.spotifyID
	elif platform == 'apple':
		targetID = query_output.appleID
	elif platform == 'youtube':
		targetID = query_output.youtubeID
	else:
		targetID = query_output.songID
	return targetID


def getOrCreateRelationship(songID, platform, song):
	#  input a songID from a supported platform and create or update row for that songID
	query_output = existsInSongPlatformModel(songID, platform)
	matchingSong = doesMatchingSongExist(song)
	if query_output is not None:  # does song exist for existing platform in db
		return query_output.songID
	elif matchingSong:  # does song exist for any platform in db
		updateSongPlatform(matchingSong, songID, platform)
		return matchingSong
	else:  # if the song does not exist yet
		new_SongID = uuid.uuid4()
		platform_relationship = SongByPlatformSerializer(data={
			platform.lower() + 'ID': songID,
			'songID': new_SongID
		})
		if platform_relationship.is_valid():
			platform_relationship.save()
	return new_SongID


def doesMatchingSongExist(song):
	try:
		query_output = Song.objects.get(title=song.title, album=song.album)
		return query_output.appSong_id
	except Exception as e:
		return None


def lookupSong(appSongID, platform):  # todo
	pass


def addSongDB(song_data):  # todo async
	serializer = SongSerializer(data=song_data)
	if serializer.is_valid(raise_exception=False):
		serializer.save()


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
