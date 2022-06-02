#!/usr/bin/env python3

import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BOARD)

def teardown():
    GPIO.cleanup()
