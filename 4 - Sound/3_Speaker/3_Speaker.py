# https://picozero.readthedocs.io/en/latest/recipes.html#speaker

from time import sleep
from picozero import Speaker

speaker = Speaker(15)

speaker.on()

speaker.freq = 200
sleep(1)

speaker.volume = .1
sleep(1)

speaker.freq = 400
sleep(1)

speaker.volume = 1
sleep(1)

speaker.off()
