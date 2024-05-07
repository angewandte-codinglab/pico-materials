# import
import network

# setup
wlan = WLAN(STA_IF)
wlan.active(True)

# loop
print(wlan.scan())