# import
from picozero import RGBLED

# setup
led = RGBLED(13, 14, 15)

# loop
led.color = (255, 255, 0)