# import
from ht16k33segment import HT16K33Segment
from machine        import I2C, Pin
from picozero       import Pot
from time           import sleep

# setup
sensor = Pot(26)

i2c = I2C(id=0, scl=5, sda=4)
led = HT16K33Segment(i2c)

threshold = sensor.value

# loop
while True:

    if sensor.value < threshold * 1.1:
        led.clear()
        led.set_number(8, 0)
        led.draw()
        
    else:
        led.clear()
        led.draw()
    
        sleep(0.5)
    
    sleep(0.001)