import os
import random

tracks = os.listdir('tracks')

track = random.choice(tracks)
print(f'Reading audio data from {track}')
with open('tracks/'+track, 'rb') as data:
    with open('playlist/output.mp3', 'wb') as out:
        print('Writing to output.mp3')
        out.write(data.read())