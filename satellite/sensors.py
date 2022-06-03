#!/usr/bin/env python3

RASPBERRY = True

try:
    import RPi.GPIO as GPIO
except:
    RASPBERRY = False

def setup():
    if not RASPBERRY:
        return

    GPIO.setmode(GPIO.BOARD)

def teardown():
    if not RASPBERRY:
        return
    
    GPIO.cleanup()
