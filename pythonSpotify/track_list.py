import spotipy
import spotipy.util as util
import pylast
import credentials

token = util.prompt_for_user_token(
    username=credentials.spotify_secrets["spotify_username"],
    scope=credentials.spotify_secrets["scope"],
    client_id=credentials.spotify_secrets["spotify_client_ID"],
    client_secret=credentials.spotify_secrets["spotify_client_secret"],
    redirect_uri=credentials.spotify_secrets["spotify_redirect_URI"])

spotify = spotipy.Spotify(auth=token)

password_hash = pylast.md5(credentials.lastfm_secrets["lastFM_password"])

network = pylast.LastFMNetwork(
    api_key=credentials.lastfm_secrets["API_KEY"],
    api_secret=credentials.lastfm_secrets["API_SECRET"],
    username=credentials.lastfm_secrets["lastFM_username"],
    password_hash=password_hash)


def track_info():
    track = spotify.current_user_playing_track()
    artist = spotify.artist(track["item"]["artists"][0]["id"])
    song = track["item"]["name"]
    album = track["item"]["album"]["name"]
    trackFM = network.get_track(artist, song)
    albumFM = network.get_album(artist, album)

# def artist_info():
#     track = spotify.current_user_playing_track()
#     artist = spotify.artist(track["item"]["artists"][0]["id"])
#     return artist
#
#
# def lastFM_track(artist, song):
#     track = network.get_track(artist, song)
#     return track
#
#
# def lastFM_album(artist, album):
#     album = network.get_album(artist, album)
#     return album