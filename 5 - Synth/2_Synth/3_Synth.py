# import
from time import sleep
from picozero import Pot, Speaker

# setup
pot     = Pot(26)
sensor  = Pot(27)
speaker = Speaker(15)

speaker.off()

# loop
while True:
    speaker.freq = 100 + int(sensor.value * 1000)
    
    print(pot.value, sensor.value)
    sleep(0.01)
    
