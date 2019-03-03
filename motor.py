#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# This file contains a driver for the stepper motor
def initMotor():
	GPIO.setmode(GPIO.BOARD)

	# Initialize the pollowing pins to gnd
	# 31, 33, 35, 37
	GPIO.setup(31, GPIO.OUT, initial=0)
	GPIO.setup(33, GPIO.OUT, initial=0)
	GPIO.setup(35, GPIO.OUT, initial=0)
	GPIO.setup(37, GPIO.OUT, initial=0)


# Turn the motor a number of steps
# Enter positive number of steps for CCW
# Enter negative number of steps for CW
def turnMotor(steps):

	inc = 0.001

	# Negative steps means turn opposite
	if (steps <= 0):
		p1 = 37
		p2 = 35
		p3 = 33
		p4 = 31
		steps = 0-steps
	else:
		p1 = 31
		p2 = 33
		p3 = 35
		p4 = 37

	while (steps > 0):
		GPIO.output(p1, GPIO.HIGH)
		time.sleep(inc)
		GPIO.output(p4, GPIO.LOW)
		time.sleep(inc)
		GPIO.output(p2, GPIO.HIGH)
		time.sleep(inc)
		GPIO.output(p1, GPIO.LOW)
		time.sleep(inc)
		GPIO.output(p3, GPIO.HIGH)
		time.sleep(inc)
		GPIO.output(p2, GPIO.LOW)
		time.sleep(inc)
		GPIO.output(p4, GPIO.HIGH)
		time.sleep(inc)
		GPIO.output(p3, GPIO.LOW)
		time.sleep(inc)

		steps = steps - 1


def deinitMotor():
	GPIO.cleanup()

