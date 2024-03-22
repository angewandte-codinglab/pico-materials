# https://picozero.readthedocs.io/en/latest/recipes.html#leds

# load the 'LED' and 'sleep' function
from picozero import LED
from time import sleep

# setup pin 15 as a LED
led = LED(15)

# turn LED on
led.on()

# wait for 1 second
sleep(1)

# turn LED off 
led.off()
