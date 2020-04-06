from genre import track
import time

count_error = 1
count_track = 1
count_play = 1
current_track = track()

if current_track is not None:
    current_song = current_track['song']

while True:
    current_track = track()

    if current_track is None:
        count_track = 1

        if count_error == 1:
            print(current_track)
            print('Error: No track is playing\n')
            count_error += 1

        count_track = 1

    else:
        count_error = 1

        if current_track["status"]:
            song_current = current_track["song"]
            time.sleep(2)
            new_track = track()

            if new_track is not None:
                song_new = new_track["song"]

                if song_new != song_current:
                    print(song_new, "-", new_track["artist"])
                    print(new_track["genre"], "\n")

                elif song_new == song_current:

                    if count_track == 1:
                        print(song_current, "-", current_track["artist"])
                        print(current_track["genre"], "\n")
                        count_track += 1

            elif count_track > 1:
                continue

            count_play = 1

        else:

            if count_play == 1:
                print('Press play button\n')
                count_track = 1
                count_play += 1

            elif count_play > 1:
                continue
