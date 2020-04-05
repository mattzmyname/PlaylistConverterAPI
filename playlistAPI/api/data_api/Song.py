class Song(object):
	def __init__(self, track_json=None):
		self.duration = 0
		self.id = 0
		self.title = ""
		self.artists = []
		self.album = ""
		self.track_number = -1
		self.genre = ""
		self.dt = None
		self.cover_image = ""
		self.query_keywords = {}

	def parseTrackJSON(self, track_json):
		if not track_json:
			return

	def __repr__(self):
		return (f'{self.__class__.__name__}('
		        f'ID : {self.id!r},\n'
		        f'Title : {self.title!r},\n'
		        f'Duration : {self.duration!r},\n'
		        f'artists : {self.artists!r},\n'
		        f'album : {self.album!r},\n'
		        f'genre : {self.genre!r},\n'
		        f'release : {self.dt!r},\n'
		        f'cover_url : {self.cover_image!r},\n')
