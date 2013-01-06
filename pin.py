import RPi.GPIO as GPIO

from utils import sleep


# init the board
GPIO.setmode(GPIO.BCM)


class Pin(object):
    """
    Represents a single output pin
    """
    def __init__(self, n):
        GPIO.setup(n, GPIO.OUT)
        self.n = n
        
    def on(self):
        GPIO.output(self.n, GPIO.HIGH)
        print self.n, 'ON'
        
    def off(self):
        GPIO.output(self.n, GPIO.LOW)
        print self.n, 'OFF'
        
    def set(self, bool):
        on(self.n) if bool else off(self.n)

    def drive(self, s, wait=None):
        self.on()
        sleep(s)
        self.off()
        if wait:
            sleep(wait)


class ExclusivePin(Pin):
    """
    A pin that mustn't be HIGH while it's counterpart is HIGH
    """
    def __init__(self, n, xpin):
        super(ExclusivePin, self).__init__(n)
        self.xpin = xpin

    def on(self):
        self.xpin.off()
        super(ExclusivePin, self).on()
