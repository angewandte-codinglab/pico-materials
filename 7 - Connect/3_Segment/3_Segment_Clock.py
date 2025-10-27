# Import
from HT16K33 import HT16K33Segment
from machine import I2C
from time    import sleep, localtime

# Setup
# Data  is connected to pin 4
# Clock is connected to pin 5
connection = I2C() 
display = HT16K33Segment(connection)

# Loop
while True:
    time = localtime()
    
    minute = str(time[4] + 100)
    second = str(time[5] + 100)
    
    print(second)
    
    display.clear()

    display.set_character(minute[1], 0)
    display.set_character(minute[2], 1)
    
    display.set_character(second[1], 2)
    display.set_character(second[2], 3)
    
    display.set_colon(True)
    display.draw()
    sleep(.5)
    
    display.set_colon(False)
    display.draw()
    sleep(.5)
