# import
from ht16k33segment import HT16K33Segment
from machine        import I2C, Pin
from picozero       import Pot
from time           import sleep
from random         import randrange

# setup
sensor = Pot(26)

i2c = I2C(id=0, scl=5, sda=4)
led = HT16K33Segment(i2c)

threshold = sensor.value

# loop
while True:
    
    value = randrange(0, 10)
    number = randrange(0, 4)
    
    led.set_number(value, number)
    led.draw()
    
    sleep(0.05)