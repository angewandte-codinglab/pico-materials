# candle animation for the internal LED

from picozero import pico_led
from random   import randrange
from time     import sleep

while 1:
    value = randrange(0, 2)
    print(value)
    
    if (value == 1):
        pico_led.on()
    else:
        pico_led.off()
        
    sleep(0.001)