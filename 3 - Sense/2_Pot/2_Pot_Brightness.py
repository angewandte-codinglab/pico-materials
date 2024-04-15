from time import sleep
from picozero import Pot, LED

pot = Pot(26)
led = LED(15)

while True:
    
    value = pot.value
    
    print(value)
    
    led.brightness = value 
    
    sleep(0.01)
