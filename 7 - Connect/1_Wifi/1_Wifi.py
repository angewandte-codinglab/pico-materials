# import
import network
from time import sleep

# setup
network.country('AT')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# loop
wlan.connect('WIFI', 'PASSWORD')
print('Connecting...')

while not wlan.isconnected():
    sleep(1)

print('Connected, IP:', wlan.ifconfig()[0])
