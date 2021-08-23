import json
import time
import os
import vlc

from glob import glob
from pygame import mixer

folder = "test"
result = {}
mp3_filenames = glob(os.path.join(folder, "*.mp3"))
for mp3 in mp3_filenames:
    print(f"Playing {mp3}")   
    song = vlc.MediaPlayer(mp3)
    song.play()
    print("Please input the noize level.")
    noise_level = input()
    while song.is_playing():
        print("Please wait until the end of the song.")
        noise_level = input()
    while noise_level not in "nc":
        print("Invalid input. Please insert 'n' for noisy or 'c' for clean.")
        noise_level = input()
    result[mp3] = noise_level

with open(os.path.join(folder, "noise_levels.json"), "w") as f:
    json.dump(result, f)