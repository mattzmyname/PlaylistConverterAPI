
import spotipy
import spotipy.util as util
import time
import credentials
import genre_finder

# If running into issue of spotipy run this on terminal to update:
# pip install git+https://github.com/plamere/spotipy.git --upgrade

token = util.prompt_for_user_token(
    username=credentials.secrets["spotify_username"],
    scope=credentials.secrets["scope"],
    client_id=credentials.secrets["spotify_client_ID"],
    client_secret=credentials.secrets["spotify_client_secret"],
    redirect_uri=credentials.secrets["spotify_redirect_URI"])

spotify = spotipy.Spotify(auth=token)

# To index artist, album, & song use:
# artist = track["item"]["artists"][0]["name"]
# song = track["item"]["name"]
# album = track["item"]["album"]["name"]

count_error = 1
count_track = 1
count_play = 1
current_track = spotify.current_user_playing_track()


if current_track is not None:
    song_current = current_track["item"]["name"]

while True:

    current_track = spotify.current_user_playing_track()

    if current_track is None:

        count_track = 1

        if count_error == 1:
            print('Error: No track is playing')
            count_error += 1

        count_track = 1

    else:
        count_error = 1
        status = current_track["is_playing"]

        if status:

            song_current = current_track["item"]["name"]
            artist_current = current_track["item"]["artists"][0]["name"]

            time.sleep(2)

            new_track = spotify.current_user_playing_track()

            if new_track is not None:
                song_new = new_track["item"]["name"]
                artist_new = new_track["item"]["artists"][0]["name"]

                if song_new != song_current:
                    print(song_new, "-", artist_new)
                    genre_finder.spotify_genre_list(new_track)
                    # count_track = 1

                elif song_new == song_current:
                    # print('1 this is current song:', song_current)
                    # print("2 this is new song:", song_new)
                    if count_track == 1:
                        print(song_current, "-", artist_current)
                        count_track += 1
                        genre_finder.spotify_genre_list(current_track)

            elif count_track > 1:
                continue

            count_play = 1

        else:
            if count_play == 1:
                print('Press play button')
                count_track = 1
                count_play += 1

            elif count_play > 1:
                continue
