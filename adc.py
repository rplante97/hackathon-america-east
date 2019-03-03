# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import datetime
import time
from w1thermsensor import W1ThermSensor
from dataProcess import *
from motor import *
from camera import *

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Hardware 1 Wire config
s = W1ThermSensor() 

try:
	# Initialize the motor
	initMotor()

	turnMotor(1, 500) # 500 steps CCW
	turnMotor(1, -500) # 500 steps CW
	turnMotor(2, 500) # 500 steps CCW
	turnMotor(2, -500) # 500 steps CW

	# Code to read ADC
	# var = mcp.read_adc(channel_num)

	# Do 5 dummy reads originally to initialize ADC
	x = mcp.read_adc(0)
	x = mcp.read_adc(1)
	x = mcp.read_adc(2)
	x = mcp.read_adc(3)
	x = mcp.read_adc(4)

	while True:

		# Read light status (int)	
		light = adc2light(mcp.read_adc(0))

		# Read temperature in C (float)
		temp = s.get_temperature()

		# Read humidity (float)
		humid = adc2humidity(mcp.read_adc(1), mcp.read_adc(2), temp)

		# Read soil moisture (integer percent)
		soil = adc2soilmoist(mcp.read_adc(3))

		# Get current time
		curr = datetime.datetime.now()
		datestring = str(curr)

		print datestring, light, " ", humid, " ", soil, temp

		time.sleep(2)

except KeyboardInterrupt:
	deinitMotor()
