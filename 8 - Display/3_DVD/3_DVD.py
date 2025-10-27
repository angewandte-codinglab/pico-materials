# import
from machine import I2C
from ssd1306 import SSD1306_I2C
from time    import sleep

# setup

width  = 128
height = 64

i2c = I2C(1, 0)
display = SSD1306_I2C(width, height, i2c, 61)

x = 0
y = 0

moveX = 1
moveY  = 1

# loop
while True:
    display.fill(0)
    display.text('DVD', x, y)
    display.show()
    
    # horizontal movement
    x = x + moveX

    if x > width - 24:
        moveX = -1
    
    if x < 0:
        moveX = 1
        
    # vertical movement   
    y = y + moveY
        
    if y > height - 8:
        moveY = -1
    
    if y < 0:
        moveY = 1
    