# import
from time    import sleep
from machine import I2C
from ssd1306 import SSD1306_I2C
from picozero import Pot, Button

# setup
xAxis = Pot(27)
yAxis = Pot(28)

switch = Button(16)

i2c = I2C() # Data: Pin 4, Clock: Pin 5
display = SSD1306_I2C(128, 64, i2c, 61)

# loop
display.fill(0)
display.show()

while True:
    x = 128 - round(xAxis.value * 128)
    y = round(yAxis.value * 64)
    
    
    display.pixel(x, y, 1)
    display.show()

    print(x, y, switch.is_pressed)
    sleep(0.01)