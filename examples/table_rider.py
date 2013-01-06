"""
This drove our first car across the in fits and starts, and
stopped before it went over the edge!
"""

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)


class Pin(object):
    def __init__(self, n):
        GPIO.setup(n, GPIO.OUT)
        self.n = n
        
    def on(self):
        GPIO.output(self.n, GPIO.HIGH)
        
    def off(self):
        GPIO.output(self.n, GPIO.LOW)
        
    def set(self, bool):
        on(self.n) if bool else off(self.n)

    def drive(self, s, wait=None):
        self.on()
        time.sleep(s)
        self.off()
        if wait:
            time.sleep(wait)
        
motor = Pin(14)

journey = 2
while journey > 0:
    hit = random.uniform(0.2, min(0.9, journey))
    wait = random.uniform(0, 1.6)

    journey -= hit
    motor.drive(hit, wait)
    print hit, journey
