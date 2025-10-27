# https://picozero.readthedocs.io/en/latest/recipes.html#buttons

from picozero import Button
from time import sleep

button = Button(15)

while True:
    print(button.is_pressed)
    sleep(0.01)