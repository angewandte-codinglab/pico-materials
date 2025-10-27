# Choose View -> Plotter in Thonny to see a graph of the results

from picozero import pico_temp_sensor, pico_led
from time import sleep

pico_led.off()

while 1:
    print(pico_temp_sensor.temp)
    
    if pico_temp_sensor.temp > 40: # when the Pico reaches 40 degrees, turn the internal LED on
        pico_led.on()
    else:
        pico_led.off()
    
    sleep(0.1)
