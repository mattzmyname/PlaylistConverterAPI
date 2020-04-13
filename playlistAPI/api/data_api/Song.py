class Song(object):
	def __init__(self, track_json=None):
		self.platform = ""
		self.duration = 0
		self.appSong_id = 0
		self.title = ""
		self.artists = []
		self.album = ""
		self.track_number = -1
		self.release_date = None
		self.cover_image_url = ""
		self.query_keywords = {}

	def parseTrackJSON(self, track_json):
		if not track_json:
			return

	def __repr__(self):
		return (f'{self.__class__.__name__}('
		        f'{self.platform} ID : {self.appSong_id!r},\n\t'
		        f'Title : {self.title!r},\n\t'
		        f'Duration : {self.duration!r},\n\t'
		        f'artists : {self.artists!r},\n\t'
		        f'album : {self.album!r},\n\t'
		        f'release : {self.release_date!r},\n\t'
		        f'track number : {self.track_number!r},\n\t'
		        f'cover_url : {self.cover_image_url!r}')
