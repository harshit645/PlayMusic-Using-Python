from pygame import mixer

#file name
file='songfile.mp3'

mixer.init()

#to load a music file
mixer.music.load(file)

#to play a music file
mixer.music.play()
