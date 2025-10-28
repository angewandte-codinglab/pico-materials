# import
from LEDStrip import LEDStrip
from machine  import SPI
from time     import sleep

# setup
spi = SPI(sck=2, mosi=3) # Configure SPI - see note below
leds = LEDStrip(spi, 8)          # Setup LED Strip with 8 LEDs

# loop
i = 0
rising = True

while True:
    leds.fill( (0, 0, 0) )
    
    leds[i] = (255, 0, 0)
    
    if rising == True:
        i = i + 1
    else:
        i = i - 1
        
    if i == 7:
        rising = False
    
    if i == 0:
        rising = True
    
    sleep(0.1)
