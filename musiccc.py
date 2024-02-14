# description: 
from earsketch import *

init()
setTempo(120)

sounds = [KHALID_NORM_BASS_808, KHALID_NORM_GUITAR_4, KHALID_NORM_DRUMBEAT]
for i in range(len(sounds)):
    sound = sounds[i]
    track = i+1
    fitMedia(sound, track, 1, 17)


finish()
