from picozero import Speaker
from random import randrange
from time import sleep

speaker = Speaker(15)
speaker.on()

while True:
    speaker.freq = randrange(200, 2000)
    sleep(randrange(1, 5) / 100)
