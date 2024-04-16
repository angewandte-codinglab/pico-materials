# https://picozero.readthedocs.io/en/latest/api.html#buzzer

from time import sleep
from picozero import Buzzer

buzzer = Buzzer(15)

buzzer.on()
sleep(3)
buzzer.off()