# import
from picozero import Pot, Servo
from time     import sleep

# setup
x = Pot(26)
y = Pot(27)

motorX = Servo(16)
motorY = Servo(17)

# loop
while True:
    motorX.value = x.value
    motorY.value = y.value
    
    print(x.value, y.value)
    sleep(0.01)