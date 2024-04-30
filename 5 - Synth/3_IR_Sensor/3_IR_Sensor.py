# import
from time import sleep
from picozero import Pot

# setup
sensor = Pot(26)

# loop
while True:
    print(sensor.value)
    sleep(0.01)
    


 