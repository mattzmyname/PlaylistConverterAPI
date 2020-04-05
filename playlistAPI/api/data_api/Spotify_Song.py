from datetime import datetime

from Song import Song


class Spotify_Song(Song):
	def __init__(self, track_json=None):
		super().__init__(track_json)
		self.query_keywords = {'name': 'getName',
		                       'artists': 'getArtists',
		                       'album': 'getAlbum',
		                       'id': 'getID',
		                       'track_number': 'getTrackNum',
		                       'duration_ms': 'getDuration',
		                       'images': 'getImage',
		                       'release_date': 'getDT'}
		self.parseTrackJSON(track_json)

	def parseTrackJSON(self, track_json):
		super()
		children_nodes = ['artists', 'album']
		try:
			for keyword in self.query_keywords.keys():
				if keyword in track_json:
					getattr(self, self.query_keywords[keyword])(track_json[keyword])
				for children in children_nodes:
					if keyword in track_json[children]:
						getattr(self, self.query_keywords[keyword])(track_json[children][keyword])
		except Exception as e:
			print(e)

	def getName(self, name):
		self.title = name

	def getID(self, id):
		self.id = id

	def getTrackNum(self, track_num):
		self.track_number = track_num

	def getArtists(self, artists):  # todo handle multiple artists
		self.artists = [artist['name'] for artist in artists]

	def getAlbum(self, album_json):
		self.album = album_json['name']

	def getDuration(self, duration):
		self.duration = duration

	def getImage(self, images):  # todo handle mutiple images
		try:
			self.cover_image = images[0]['url']
		except:
			print("missing image url")

	def getDT(self, release):
		self.dt = datetime.strptime(release, '%Y-%m-%d')
