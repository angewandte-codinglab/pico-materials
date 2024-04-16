from picozero import Pot
from time import sleep

pot = Pot(26)

while True:
    print(pot.value)
    sleep(0.01)