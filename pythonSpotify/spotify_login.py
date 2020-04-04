import pylast
import credentials
import spotipy
import spotipy.util as util




def auth():
    token = util.prompt_for_user_token(
        username=credentials.secrets["spotify_username"],
        scope=credentials.secrets["scope"],
        client_id=credentials.secrets["spotify_client_ID"],
        client_secret=credentials.secrets["spotify_client_secret"],
        redirect_uri=credentials.secrets["spotify_redirect_URI"])

    spotify_auth = spotipy.Spotify(auth=token)

    return spotify_auth
