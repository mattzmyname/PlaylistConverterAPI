import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

from .Playlist import Playlist
from .Spotify_Song import Spotify_Song


class Spotify(object):
	def __init__(self, username=""):
		self.client_credentials_manager = SpotifyClientCredentials()
		self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
		self.username = username
		if username:
			scope = "playlist-modify-public"
			token = util.prompt_for_user_token(username, scope)
			if token:
				self.sp = spotipy.Spotify(auth=token)
			else:
				print("Can't get token for", username)

	def createPlaylist(self, name="test1", songList=None):
		if songList is None:
			songList = []
		if self.username:
			newPlaylist = self.sp.user_playlist_create(user=self.username, name=name)
			newPlaylistID = newPlaylist['id']
			print(self.sp.user_playlist_add_tracks(self.username, newPlaylistID, songList))
			return True
		return False

	def parsePlaylist(self, playlistURL):
		song_list = []
		playlist = self.sp.playlist(playlistURL.strip())
		playlistName = playlist['name']
		for track in playlist['tracks']['items']:
			track_id = track['track']['id']
			song_list.append(Spotify_Song(self.getTrack(track_id)))
		return Playlist(playlistName, song_list)

	def getTrack(self, uri):
		return self.sp.track(uri)


if __name__ == '__main__':
	spotify = Spotify()
	top_songs = 0
	with open("sample_playlists.txt", "r") as a_file:
		for line in a_file:
			songs = spotify.parsePlaylist(line)
			print(songs)
