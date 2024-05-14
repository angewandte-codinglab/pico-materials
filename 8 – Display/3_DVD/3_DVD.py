# import
from machine import SoftI2C
from ssd1306 import SSD1306_I2C
from time    import sleep

# setup

width  = 128
height = 64

i2c = SoftI2C(1, 0)
display = SSD1306_I2C(width, height, i2c, 61)

x = 0
y = 0

moveRight = 1
moveDown  = 1

# loop
while True:
    display.fill(0)
    display.text('DVD', x, y)
    display.show()
    
    # horizontal movement
    x = x + moveRight

    if x > width - 24:
        moveRight = -1
    
    if x < 0:
        moveRight = 1
        
    # vertical movement   
    y = y + moveDown
        
    if y > height - 8:
        moveDown = -1
    
    if y < 0:
        moveDown = 1
    