"""
This was the first go at reading an input pin and
getting some LEDs to turn on and off in response

LED on, LED off... hence karate kid ;-)
"""

import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

GPIO.setup(1, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

def on(n):
    GPIO.output(n, GPIO.HIGH)
def off(n):
    GPIO.output(n, GPIO.LOW)
def turn(n, bool):
    on(n) if bool else off(n)
    


while True:
    val = GPIO.input(17)
    print val

    turn(1, not val)
    turn(14, val)
    time.sleep(1)
    
