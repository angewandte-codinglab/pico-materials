# import
from LEDStrip import LEDStrip
from machine  import SPI
from time     import sleep

# setup
spi = SPI() # Configure SPI - see note below
leds = LEDStrip(spi, 8)          # Setup LED Strip with 8 LEDs

# loop
i = 0

while i < 8:
    
    leds[i] = (255, 0, 0)
    
    i = i + 1
    
    sleep(0.2)