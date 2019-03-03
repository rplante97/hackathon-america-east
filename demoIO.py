#!/usr/bin/python

import time
from motor import *
from outputs import *


try:
	motor1stat = 1
	motor2stat = 1
	initMotor()
	initIO()

	# Loop forever
	while True:
		# Check buttons
		lightUpdate(lightButtonRead())

		if (motor1ButtonRead()):
			turnMotor(1, 2000 * motor1stat)
			motor1stat = 0-motor1stat
			# Wait for button release
			while (motor1ButtonRead()):
				time.sleep(0.001)

		if (motor2ButtonRead()):
			turnMotor(2, 2000 * motor2stat)
			motor2stat = 0-motor2stat
			# Wait for button release
			while (motor1ButtonRead()):
				time.sleep(0.001)

		time.sleep(0.005)

	IOcleanup()
	deinitMotor()


except KeyboardInterrupt:
	IOcleanup()
