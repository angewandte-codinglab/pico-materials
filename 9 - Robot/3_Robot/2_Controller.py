# import
from picozero import Pot, Servo
from time     import sleep

# setup
knob = Pot(26)
motor = Servo(16)

# loop
while True:    
    motor.value = knob.value
    
    print(knob.value)
    sleep(0.01)