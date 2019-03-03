#!/usr/bin/python

from picamera import PiCamera
import time

def savePhoto(filePath):
	
	# Initialize cam
	cam = PiCamera()

	# Begin preview
	cam.start_preview()

	# Wait for light to adjust
	time.sleep(2)

	# Capture photo and save to 
	cam.capture(filePath)
	
	# Stop preview
	cam.stop_preview()
