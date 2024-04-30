from machine import Pin
from time    import sleep

mic = Pin(26, Pin.IN)

while True:
    
    if mic.value() == 1:  
    
        print('Snap')
        sleep(0.1)