# from Library  import Function
from picozero import pico_led
from time     import sleep

# turn the internal Pico LED on and off

while 1:
  sleep(1)
  pico_led.on()
  sleep(1)
  pico_led.off()
