#import json
#import genre
#from track_list import track_info as track
from genre import track
#from genre import Genre_list
import time
# import spotipy
# import spotip
# y.util as util
# import credentials
#
# token = util.prompt_for_user_token(
#     username=credentials.secrets["spotify_username"],
#     scope=credentials.secrets["scope"],
#     client_id=credentials.secrets["spotify_client_ID"],
#     client_secret=credentials.secrets["spotify_client_secret"],
#     redirect_uri=credentials.secrets["spotify_redirect_URI"])
#
# spotify_auth = spotipy.Spotify(auth=token)

# To index artist, album, & song use:
# artist = track["item"]["artists"][0]["name"]
# song = track["item"]["name"]
# album = track["item"]["album"]["name"]

#print('Error: No track is playing')
count_error = 1
count_track = 1
count_play = 1
current_track = track()

#current_json = json.dumps(current_track)
#print(current_json)
#print(current_track)

# GET https://api.spotify.com/v1/artists/{id}

# artist_id = current_track["item"]["artists"][0]["id"]
# album_id = current_track["item"]["album"]["id"]
# print(artist_id)
# print(album_id)

# request_link = 'https://api.spotify.com/v1/artists/{' + artist_id + '}'
# print(request_link)
# genre = requests.get(request_link)

# artist_info = spotify.artist(artist_id)
# album_info = spotify.album(album_id)
# info_json = json.dumps(album_info)
# print(info_json)
# genres2 = album_info
# genres = artist_info["genres"]
# print(genres)

# info_json = json.dumps(artist_info)
# print(info_json)
# print(artist_info)
# print(genre)

if current_track is not None:
    current_track = track()
    current_song = current_track['song']

while True:
    # if current_track is None:
    #     none1 = current_track
    #     while none1 is None:
    #         none2 = spotify.current_user_playing_track()
    #
    #         if none1 != none2:
    #             print('Error: No track is playing')
    #         else:
    #             break
    current_track = track()

    if current_track is None:
        # player_status = 'off'
        # if player_status != 'off':
        #     continue
        count_track = 1

        if count_error == 1:
            print('Error: No track is playing')
            count_error += 1

        # elif count_error > 1:
        #     continue

        count_track = 1

    else:


        # time.sleep(2)
        # new_track = spotify.current_user_playing_track()


        count_error = 1
        # new_track = spotify.current_user_playing_track()
        # track_json = json.dumps(new_track)
        # song_current = current_track["item"]["name"]
        current_track = track()
        status = current_track["status"]
        #status = str(status)



        if status:

            song_current = current_track["song"]
            artist_current = current_track["artist"]
            genres = current_track["genre"]

            time.sleep(2)

            new_track = track()

            if new_track is not None:
                song_new = new_track["song"]
                artist_new = new_track["artist"]
                genres = new_track["genre"]

                if song_new != song_current:
                    print(song_new, "-", artist_new)
                    print(genres, "\n")
                    # count_track = 1

                elif song_new == song_current:
                    # print('1 this is current song:', song_current)
                    # print("2 this is new song:", song_new)
                    if count_track == 1:

                        print(song_current, "-", artist_current)
                        print(genres, "\n")
                        count_track += 1

            # else:
            #     continue


            #print(song_new)
            #print(song_current)
            # print(song_new)
            # print(song_current)
            #if count_track == 1:

            # if song_new != song_current:
            #     print(song_new, "-", artist_new)
            #     genre_finder.spotify_genre_list(new_track)
            #     #count_track = 1
            #
            # elif song_new == song_current:
            #     # print('1 this is current song:', song_current)
            #     # print("2 this is new song:", song_new)
            #     if count_track == 1:
            #         print(song_current, "-", artist_current)
            #         count_track += 1
            #         genre_finder.spotify_genre_list(current_track)


                # print(song_current)
                # count_track += 1

            # elif count_track == 2:
            #     print(song_new)
            #     count_track += 1
                # if song_new == song_current:
                #
                #     # song = current_track["item"]["name"]
                #
                # elif song_new != song_current:
                #     continue

            elif count_track > 1:
                continue

            count_play = 1

        else:
            if count_play == 1:
            # print(status.title())
                print('Press play button')
                count_track = 1
                count_play += 1

            elif count_play > 1:
                continue
            # print(artist)
            # print(song)
    # current_track = spotify.current_user_playing_track()
 #   print('Here is current track: ' + str(current_track))
# status = track_json['object']['context'][0]['name']