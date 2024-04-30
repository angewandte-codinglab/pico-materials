from machine import Pin, SPI
from time import sleep
from ledstrip import LEDStrip

mic = Pin(26, Pin.IN)

spi = SPI(id=0, sck=2, mosi=3) # Configure SPI - see note below
leds = LEDStrip(spi, 8)        # Setup LED Strip with 8 LEDs

while True:
    
    if mic.value() == 1:  
    
        for x in range(8):

            leds[x] = (128, 0, 0)
            sleep(0.01)
            leds.fill((0, 0, 0))