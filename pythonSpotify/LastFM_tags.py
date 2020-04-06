import pylast
# import json
# import xmltodict

username = "jowpow"

password_hash = pylast.md5("9512369Jp!")

API_KEY = '9fb2ee7a3b730de8f8f0965c94e727bf'

API_SECRET = '1c9e946524aa297b5f5f96bb5445367f'


network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

def track_top_tags(artist, track):

    import pylast
    username = "jowpow"

    password_hash = pylast.md5("9512369Jp!")

    API_KEY = '9fb2ee7a3b730de8f8f0965c94e727bf'

    API_SECRET = '1c9e946524aa297b5f5f96bb5445367f'

    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=username, password_hash=password_hash)

    track = network.get_track(artist, track)

    track_tags_list = track.get_top_tags()

    list = []
    count = 0

    for value in range(0, len(track_tags_list)):
        tag = str(track_tags_list[count][0])
        list.append(tag)
        count += 1

    print(list)

def album_top_tags(artist, album):
    import pylast
    username = "jowpow"

    password_hash = pylast.md5("9512369Jp!")

    API_KEY = '9fb2ee7a3b730de8f8f0965c94e727bf'

    API_SECRET = '1c9e946524aa297b5f5f96bb5445367f'

    network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                                   username=username, password_hash=password_hash)

    album = network.get_album(artist, album)

    album_tags_list = album.get_top_tags()

    list = []
    count = 0

    for value in range(0, len(album_tags_list)):
        tag = str(album_tags_list[count][0])
        list.append(tag)
        count += 1

    print(list)


track = network.get_track("Frank Ocean", "Self Control")
print(track)
track_tags_list = track.get_top_tags()
# info_json = json.dumps(track.get_top_tags())

# artist = network.search_for_artist("Tyler, the Creator")

# print(artist)

# artist_name = artist.get_artist_info()

album = network.get_album("Tyler, the Creator", "Flower Boy")
album_tags_list = album.get_top_tags()

print("\nalbum:", album)
print(album_tags_list)
print("\nAlbum genre:", album_tags_list[1][0], "\n")
print(track_tags_list)


# print(len(track_tags_list))
print("\nTrack genre:", track_tags_list[0][0], '\n')
# print(track_tags_list[1][0])
# print(track_tags_list[2][0])
# print(track_tags_list[3][0])
# print(track_tags_list[4][0])

list = []
count = 0

for value in range(0, len(track_tags_list)):
    tag = str(track_tags_list[count][0])
    list.append(tag)
    count += 1
print(list)
# track_tags = xmltodict(track_tags_xml)
# print(track_tags)

# tags[TopItem]
# print(tags<'TopItem'>)