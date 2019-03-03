#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# This file contains a driver for the stepper motor
def initMotor():
	GPIO.setmode(GPIO.BOARD)

	# Initialize the Motor 1 pins to gnd
	# 31, 33, 35, 37
	GPIO.setup(31, GPIO.OUT, initial=0)
	GPIO.setup(33, GPIO.OUT, initial=0)
	GPIO.setup(35, GPIO.OUT, initial=0)
	GPIO.setup(37, GPIO.OUT, initial=0)


	# Initialize the Motor 2 pins to gnd
	# 32, 36, 38, 40
	GPIO.setup(32, GPIO.OUT, initial=0)
	GPIO.setup(36, GPIO.OUT, initial=0)
	GPIO.setup(38, GPIO.OUT, initial=0)
	GPIO.setup(40, GPIO.OUT, initial=0)


# Turn the motor a number of steps
# Enter positive number of steps for CCW
# Enter negative number of steps for CW
def turnMotor(motorNum, steps):

	inc = 0.001

	# Check for correct motor numbers
	if (motorNum != 1 and motorNum != 2): return

	if (motorNum == 1):
		p1, p2, p3, p4 = 31, 33, 35, 37
	else:
		p1, p2, p3, p4 = 32, 36, 38, 40

	# Negative steps means turn opposite
	if (steps <= 0):
		p1, p2, p3, p4 = p4, p3, p2, p1
		steps = 0-steps

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

