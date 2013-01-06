import time
import contextlib

from pin import Pin, ExclusivePin
from utils import sleep

    
class Car(object):
    """
    Control of our lego buggy via left, right and gas pins
    """
    def __init__(self):
        self.left = ExclusivePin(17, None)
        self.right = ExclusivePin(14, self.left)
        self.gas = Pin(0)
        self.left.xpin = self.left
        
    def turn(self, s, is_left, angle=0.05):
        first = self.left if is_left else self.right
        second = self.right if is_left else self.left
        first.drive(angle)
        end = time.time() + s
        while time.time() < end:
            sleep(0.25)
            first.drive(angle/10)
        second.drive(angle)

    def turn_left(self, s):
        self.turn(s, True)
        
    def turn_right(self, s):
        self.turn(s, False)

    def rev(self, s=0.4):
        self.gas.drive(s)

    def start(self, wait=None):
        self.gas.on()
        if wait:
            sleep(wait)

    def pause(self, s):
        self.stop()
        sleep(s)
        self.start()
        
    def stop(self):
        self.gas.off()
        
    def all_stop(self):
        self.stop()
        self.left.off()
        self.right.off()

@contextlib.contextmanager
def safe_car():
    """
    Make sure the car (ie code) doesn't crash with the
    accelerator (or steering) stuck on
    """
    car = Car()
    try:
        yield car
    finally:
        car.all_stop()

def loop():
    """
    Do a little loop round the table
    """
    with safe_car() as car:
        car.start(0.2)
        car.pause(1)
        car.turn_right(2.75)
        car.pause(1)
        car.start(0.3)

def wiggle(s=0.1):
    """
    Drive across the table with a little wiggle in yo ass
    """
    with safe_car() as car:
        car.start(s)
        car.turn_left(s)
        sleep(s)
        car.turn_right(s)
        sleep(s)
        loop()
