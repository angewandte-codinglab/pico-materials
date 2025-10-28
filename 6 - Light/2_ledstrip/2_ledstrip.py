# import
from LEDStrip import LEDStrip
from machine  import SPI

# setup
spi = SPI(sck=2, mosi=3) # Configure SPI - see note below
leds = LEDStrip(spi, 8)          # Setup LED Strip with 8 LEDs

# loop
leds[0] = (128, 0, 0) # Set the first LED to red 
leds.fill((0,0,255))  # Set all LEDs to blue
