from time import sleep
from picozero import Pot

pot = Pot(26)

while True:
    print(pot.value)
    sleep(0.1)