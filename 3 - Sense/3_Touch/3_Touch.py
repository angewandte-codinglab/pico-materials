from Touchpad import Touchpad
from picozero import LED
from time import sleep

touch = Touchpad(1)
led   = LED(14)

while True:
    touch.update()
    level = touch.level
    print(level)
    
    if (level > 0.75):
        led.on()
    else:
        led.off()
    
    sleep(0.01)