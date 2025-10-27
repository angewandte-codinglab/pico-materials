from Touchpad import Touchpad
from picozero import LED, Pot
from time import sleep

touch = Touchpad(1)
led   = LED(14)
pot   = Pot(26)

while True:
    touch.update()
    level = touch.level
    print(level, pot.value)
    
    if (level > pot.value):
        led.on()
    else:
        led.off()
    
    sleep(0.01)
