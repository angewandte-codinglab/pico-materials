# import
from picozero import Pot, Servo
from time     import sleep

# setup
motor = Servo(16)

# loop
while True:
    motor.value = 0
    sleep(0.3)
    motor.value = 1
    sleep(0.3)
    motor.value = 0

    sleep(5)