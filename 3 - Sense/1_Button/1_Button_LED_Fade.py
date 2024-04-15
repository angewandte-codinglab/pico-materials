# https://picozero.readthedocs.io/en/latest/recipes.html#buttons

from picozero import Button, LED
from time import sleep

button = Button(15)
led    = LED(14)

while True:
    
    if button.is_pressed:
        led.brightness = led.brightness + 0.001
    else:
        led.brightness = 0
        
    print(button.is_pressed)
    
    sleep(0.01)

