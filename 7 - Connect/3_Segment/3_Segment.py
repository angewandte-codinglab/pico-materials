# import
from ht16k33segment import HT16K33Segment
from machine import I2C, Pin
from time import sleep

# setup
i2c = I2C(id=0, scl=Pin(5), sda=Pin(4))
led = HT16K33Segment(i2c)

# loop
led.clear()

led.set_number(1, 0)
led.set_number(2, 1)
led.set_number(3, 2)
led.set_number(4, 3)

led.set_colon(True)

led.draw()

while True:
    led.set_colon(True)
    led.draw()
    
    sleep(0.5)
    
    led.set_colon(False)
    led.draw()
    
    sleep(0.5)