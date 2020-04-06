# Getting the tracks album, artist, song name, and artist id
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

class Track():
    """Getting the track info"""


    def __init__(self, track):

        self.artist = track["item"]["artists"][0]["name"]
        self.song = track["item"]["name"]
        self.album = track["item"]["album"]["name"]
       # self.artist_id = track["item"]["artists"][0]["id"]
        self.artist_info = spotify.artist(track["item"]["artists"][0]["id"])

track1 = {'timestamp': 1559182765728, 'context': {'external_urls': {'spotify': 'https://open.spotify.com/artist/0tvpihdAsKiNnP6sWS3jUI'}, 'href': 'https://api.spotify.com/v1/artists/0tvpihdAsKiNnP6sWS3jUI', 'type': 'artist', 'uri': 'spotify:artist:0tvpihdAsKiNnP6sWS3jUI'}, 'progress_ms': 232802, 'item': {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0tvpihdAsKiNnP6sWS3jUI'}, 'href': 'https://api.spotify.com/v1/artists/0tvpihdAsKiNnP6sWS3jUI', 'id': '0tvpihdAsKiNnP6sWS3jUI', 'name': 'TroyBoi', 'type': 'artist', 'uri': 'spotify:artist:0tvpihdAsKiNnP6sWS3jUI'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'external_urls': {'spotify': 'https://open.spotify.com/album/6FJ6fO4MeunhgpoG4sg0xH'}, 'href': 'https://api.spotify.com/v1/albums/6FJ6fO4MeunhgpoG4sg0xH', 'id': '6FJ6fO4MeunhgpoG4sg0xH', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/476805f838a0fffdaa09146b8317df0966845a13', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/c9783a920afeaa18c00f9cd9d2cbaa1e7d17deec', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/473e243f771949a1cd7e258e4fb01d2a9f9a3776', 'width': 64}], 'name': 'Afterhours feat. Diplo & Nina Sky', 'release_date': '2015-09-18', 'release_date_precision': 'day', 'total_tracks': 1, 'type': 'album', 'uri': 'spotify:album:6FJ6fO4MeunhgpoG4sg0xH'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/0tvpihdAsKiNnP6sWS3jUI'}, 'href': 'https://api.spotify.com/v1/artists/0tvpihdAsKiNnP6sWS3jUI', 'id': '0tvpihdAsKiNnP6sWS3jUI', 'name': 'TroyBoi', 'type': 'artist', 'uri': 'spotify:artist:0tvpihdAsKiNnP6sWS3jUI'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5fMUXHkw8R8eOP2RNVYEZX'}, 'href': 'https://api.spotify.com/v1/artists/5fMUXHkw8R8eOP2RNVYEZX', 'id': '5fMUXHkw8R8eOP2RNVYEZX', 'name': 'Diplo', 'type': 'artist', 'uri': 'spotify:artist:5fMUXHkw8R8eOP2RNVYEZX'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/6eBYLQONaYZhZNAVK061t6'}, 'href': 'https://api.spotify.com/v1/artists/6eBYLQONaYZhZNAVK061t6', 'id': '6eBYLQONaYZhZNAVK061t6', 'name': 'Nina Sky', 'type': 'artist', 'uri': 'spotify:artist:6eBYLQONaYZhZNAVK061t6'}], 'available_markets': ['AD', 'AE', 'AR', 'AT', 'AU', 'BE', 'BG', 'BH', 'BO', 'BR', 'CA', 'CH', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DE', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'FI', 'FR', 'GB', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IE', 'IL', 'IN', 'IS', 'IT', 'JO', 'JP', 'KW', 'LB', 'LI', 'LT', 'LU', 'LV', 'MA', 'MC', 'MT', 'MX', 'MY', 'NI', 'NL', 'NO', 'NZ', 'OM', 'PA', 'PE', 'PH', 'PL', 'PS', 'PT', 'PY', 'QA', 'RO', 'SA', 'SE', 'SG', 'SK', 'SV', 'TH', 'TN', 'TR', 'TW', 'US', 'UY', 'VN', 'ZA'], 'disc_number': 1, 'duration_ms': 275604, 'explicit': False, 'external_ids': {'isrc': 'USZ4V1500152'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/1gV0hgMNdpSWeW7ZjSUKnX'}, 'href': 'https://api.spotify.com/v1/tracks/1gV0hgMNdpSWeW7ZjSUKnX', 'id': '1gV0hgMNdpSWeW7ZjSUKnX', 'is_local': False, 'name': 'Afterhours feat. Diplo & Nina Sky', 'popularity': 58, 'preview_url': 'https://p.scdn.co/mp3-preview/cc7eba2c570444057d03a06e991df9fba52a2f6b?cid=84b2a106838b4135b2ba33bbb0b24df5', 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:1gV0hgMNdpSWeW7ZjSUKnX'}, 'currently_playing_type': 'track', 'actions': {'disallows': {'resuming': True}}, 'is_playing': True}


print(Track(track1).artist)
