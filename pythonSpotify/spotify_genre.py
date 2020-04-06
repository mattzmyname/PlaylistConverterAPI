import spotipy
import spotipy.util as util

# Spotify username
username = '12175470220'
# Spotify scope
scope = 'user-read-currently-playing'
# Spotify client ID
c_id = '84b2a106838b4135b2ba33bbb0b24df5'
# Spotify client secret
c_secret = '46c43d71bc16425cab098353d03467fb'
# Spotify redirect URI
redirect_URI = 'http://localhost:8888/callback'

token = util.prompt_for_user_token(username, scope, client_id=c_id, client_secret=c_secret, redirect_uri=redirect_URI)
spotify = spotipy.Spotify(auth=token)

def spotify_genre_list(track):

    import spotipy
    import spotipy.util as util

    # Spotify username
    username = '12175470220'
    # Spotify scope
    scope = 'user-read-currently-playing'
    # Spotify client ID
    c_id = '84b2a106838b4135b2ba33bbb0b24df5'
    # Spotify client secret
    c_secret = '46c43d71bc16425cab098353d03467fb'
    # Spotify redirect URI
    redirect_URI = 'http://localhost:8888/callback'

    token = util.prompt_for_user_token(username, scope, client_id=c_id, client_secret=c_secret,
                                       redirect_uri=redirect_URI)
    spotify = spotipy.Spotify(auth=token)
    artist_id = track["item"]["artists"][0]["id"]
    artist_info = spotify.artist(artist_id)
    genres = artist_info["genres"]
    print(genres)
