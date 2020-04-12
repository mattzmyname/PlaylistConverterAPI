import uuid


class Playlist(object):
	def __init__(self, name=uuid.uuid4(), songs=None):
		if songs is None:
			songs = []
		self.name = name
		self.songs = songs
