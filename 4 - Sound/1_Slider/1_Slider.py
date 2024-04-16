# https://picozero.readthedocs.io/en/latest/recipes.html#potentiometer

from time import sleep
from picozero import Pot

slider = Pot(26)

while True:    
    print(slider.value)
    sleep(0.1)