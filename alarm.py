import pyglet
import time
# plays alarm sound
PATH_TO_REPO = '/Users/gpena/Documents/LeetCodeAlarm/'
music = pyglet.media.load(f'{PATH_TO_REPO}danger.mp3')
music.play()
time.sleep(7.2)
exit(0)