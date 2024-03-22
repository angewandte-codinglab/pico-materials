# https://picozero.readthedocs.io/en/latest/recipes.html#leds

# load the 'LED' and 'sleep' function
from picozero import LED
from time import sleep

# setup pin 15 as a LED
led = LED(15)

# endless loop
while True:
    # turn LED on
    led.on()
    
    # wait for half a second
    sleep(0.5)
    
    # turn LED off again
    led.off()
    
    # wait for a second
    sleep(1)
