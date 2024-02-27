# description: 
from earsketch import *

init()
setTempo(120)

sounds = [ELECTRO_DRUM_MAIN_LOOPPART_038, RD_EDM_CHORDPART_3]
for i in range(len(sounds)):
    sound = sounds[i]
    track = i+1
    fitMedia(sound, track, 1, 17)

finish()
