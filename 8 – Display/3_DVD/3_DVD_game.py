# import
from machine  import SoftI2C
from ssd1306  import SSD1306_I2C
from picozero import Pot

# setup

width  = 128
height = 64

pot = Pot(26)
i2c = SoftI2C(1, 0)
display = SSD1306_I2C(width, height, i2c, 61)

textWidth = 24

x = 0
y = 0

moveRight = 1
moveDown  = 1

score = 0
record = 0

# loop
while True:
    pos = round(pot.value * (width - textWidth))

    display.fill(0)
    display.text('Score:' + str(score), 0, 0)
    display.text('Record:' + str(record), 0, 8)
    display.text('DVD', x, y)
    display.hline(pos, 63, textWidth, 1)
    display.show()

    # horizontal movement
    x = x + moveRight

    if x > width - 24 or x < 0:
        moveRight = moveRight * -1
        
    # vertical movement   
    y = y + moveDown
        
    if y > height - 8:
        if x > pos - textWidth and x < pos + textWidth:      
            moveDown = moveDown * -1
            score = score + 1
            if score > record:
                record = score
        else:
            y = 0
            score = 0
    
    if y < 0:
        moveDown = moveDown * -1   