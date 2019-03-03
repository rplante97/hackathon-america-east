#!/usr/bin/python

import RPi.GPIO as GPIO

# This file controls the motors, buttons, and leds

def initIO():
	GPIO.setmode(GPIO.BOARD)

	# Initialize the lights pin
        GPIO.setup(10, GPIO.OUT, initial=0)

	# Initialize the light button
        GPIO.setup(12, GPIO.IN, initial=0)

	# Initialize the motor 1 button
        GPIO.setup(13, GPIO.IN, initial=0)

	# Initialize the motor 2 button
        GPIO.setup(15, GPIO.IN, initial=0)

def lightUpdate(val):
	# 0 = off
	# else = on
	if (val == 0):
		GPIO.output(10, GPIO.LOW)
	else:
		GPIO.output(10, GPIO.HIGH)

def lightButtonRead():
	# Read pin 12, button that controls the light
	return GPIO.input(12)

def motor1ButtonRead():
	# Read pin 13, button that controls motor 1
	return GPIO.input(13)

def motor2ButtonRead():
	# Read pin 15, button that controls motor 2
	return GPIO.input(15)

def IOcleanup():
	GPIO.cleanup()
