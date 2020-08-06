#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time


GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(3, GPIO.IN)

# turn on the switched power supply
GPIO.output(16, 1)

st = 0
while True:
    GPIO.wait_for_edge(3, GPIO.RISING)
    et = time.time() - st
    print("et="+str(et))
    if (et > .1 and et < .5):
        break
    else:
        st = time.time()

print("shutdown")
subprocess.call(['shutdown', '-h', 'now'], shell=False)
