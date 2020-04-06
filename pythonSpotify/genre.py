import credentials
import spotipy
import spotipy.util as util


def track():

    token = util.prompt_for_user_token(
        username=credentials.secrets["spotify_username"],
        scope=credentials.secrets["scope"],
        client_id=credentials.secrets["spotify_client_ID"],
        client_secret=credentials.secrets["spotify_client_secret"],
        redirect_uri=credentials.secrets["spotify_redirect_URI"])

    spotify_auth = spotipy.Spotify(auth=token)
    track = spotify_auth.current_user_playing_track()

    if track is not None:
        artist_info = spotify_auth.artist(track["item"]["artists"][0]["id"])
        track_info = {
            'status': track["is_playing"],
            'song': track["item"]["name"],
            'artist': track["item"]["artists"][0]["name"],
            'genre': artist_info["genres"]
                      }
        return track_info

    elif track is None:
        return track
