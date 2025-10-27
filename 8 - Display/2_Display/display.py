# import
from machine import I2C
from ssd1306 import SSD1306_I2C
from time    import sleep

# setup
i2c = I2C() # Data: Pin 4, Clock: Pin 5
display = SSD1306_I2C(128, 64, i2c, 61)

# loop
display.fill(0)
display.text('Hello!', 0, 0)
display.show()

display.pixel(64,32,1)
display.show()



