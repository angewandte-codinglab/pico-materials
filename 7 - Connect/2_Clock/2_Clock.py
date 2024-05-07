# import
from machine import RTC

# setup
clock = RTC()

# loop
time = clock.datetime()

print(time)

minute = time[5]
hour = time[4]

print(hour, minute)