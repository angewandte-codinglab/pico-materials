# Import
from machine import I2C

# Setup
# Data  is connected to pin 4
# Clock is connected to pin 5
i2c = I2C() 

# Loop
print(i2c.scan())
