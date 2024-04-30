# import
from picozero import RGBLED
from time     import sleep
from random   import randrange

# setup
led = RGBLED(13, 14, 15)

# loop
while True:
    red   = randrange(0, 256)
    green = randrange(0, 256)
    blue  = randrange(0, 256)
    
    led.color = (red, green, blue)
    
    sleep(1)