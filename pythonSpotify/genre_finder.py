
artist = "Frank Ocean"
track = "Self Control"

def genre_list(album, artist, song, track):
    """Getting the track, album, or artist's genre.
    First looking for track genre, then album genre,
    then artist genre."""

    track = track
    album = album
    artist = artist
    song = song

    import spotipy
    import spotipy.util as util
    import pylast

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

    # LastFM Info:
    # LastFM username
    username = "jowpow"
    # LastFM password
    password_hash = pylast.md5("9512369Jp!")
    # LastFM api key
    API_KEY = '9fb2ee7a3b730de8f8f0965c94e727bf'
    # LastFM api secret
    API_SECRET = '1c9e946524aa297b5f5f96bb5445367f'

    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=username, password_hash=password_hash)

    def track_top_tags(artist, song):
        """Looking for the track genre using the LastFM track top tags"""

        track = network.get_track(artist, song)

        track_tags_list = track.get_top_tags()

        list = []
        count = 0

        for value in range(0, len(track_tags_list)):
            tag = str(track_tags_list[count][0])
            list.append(tag)
            count += 1

        print(list)

    track_top_tags(artist, song)

    def album_top_tags(artist, album):
        """Looking for the album genre using the LastFM album top tags"""

        album = network.get_album(artist, album)

        album_tags_list = album.get_top_tags()

        list = []
        count = 0

        for value in range(0, len(album_tags_list)):
            tag = str(album_tags_list[count][0])
            list.append(tag)
            count += 1

        print(list)

    album_top_tags(artist, album)

    def spotify_genre_list(track):

        artist_id = track["item"]["artists"][0]["id"]
        artist_info = spotify.artist(artist_id)
        genres = artist_info["genres"]
        print(genres)

    spotify_genre_list(track)


# track_Top_tags(artist, track)


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