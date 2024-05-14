# import
from machine import SoftI2C

# setup
i2c = SoftI2C(1, 0)

# loop
print(i2c.scan())