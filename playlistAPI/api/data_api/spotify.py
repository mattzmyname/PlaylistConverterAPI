import spotipy
from Spotify_Song import Spotify_Song
from spotipy.oauth2 import SpotifyClientCredentials


class Spotify(object):
	def __init__(self):
		self.client_credentials_manager = SpotifyClientCredentials()
		self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

	def parsePlaylist(self, playlistURL):
		song_list = []
		playlist = self.sp.playlist(playlistURL.strip())
		for track in playlist['tracks']['items']:
			track_id = track['track']['id']
			song_list.append(Spotify_Song(self.getTrack(track_id)))
		return song_list

	def getTrack(self, uri):
		return self.sp.track(uri)


if __name__ == '__main__':
	spotify = Spotify()
	top_songs = 0
	with open("sample_playlists.txt", "r") as a_file:
		for line in a_file:
			songs = spotify.parsePlaylist(line)
			print(songs)
