from machine  import Pin, SPI
from time     import sleep
from ledstrip import LEDStrip
from random   import randrange

mic = Pin(26, Pin.IN)

spi = SPI(id=0, sck=2, mosi=3) # Configure SPI - see note below
leds = LEDStrip(spi, 8)        # Setup LED Strip with 8 LEDs

while True:
    
    if mic.value() == 1:
        print('Snap')
        
        color = (randrange(256), randrange(256), randrange(256))
        
        leds.fill(color)