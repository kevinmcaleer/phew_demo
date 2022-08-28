# demo1.py - Install Phew using upip
# Kevin McAleer
# 28 Aug 2022

from secret import ssid, password
import network
from time import sleep

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

if wlan.isconnected == False:
    sleep(0.1)

print("connected to wifi")

import upip
upip.install("micropython-phew")
