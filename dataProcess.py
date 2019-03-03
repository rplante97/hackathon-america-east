#!/usr/bin/python

import math

# This file processes data obtained by the ADC
# It converts sample data to measurable data

# Convert ADC light value to light description
def adc2light(val):

	if (val < 0 or val > 1023):
		return "Invalid value"

	# 1023 -> No light
	# 0 -> Max light
	if (val < 200):
		# 0-199
		return 0
	elif (val < 500):
		# 200-499
		return 1
	elif (val < 750):
		# 500-749
		return 2
	elif (val < 900):
		# 750-899
		return 3
	else:
		# 899-1023
		return 4


# Convert ADC humidity value to humidity percent
def adc2humidity(val1, val2, temp):

	# val1 = value of low humidity sensor
	# val2 = vlaue of high humidity sensor
	# temp = temperature, deg C

	if (val1 <= 0 or val1 > 1023 or val2 <= 0 or val2 > 1023):
		return -1

	# Determine humidity based on val1 reading
	# Find resistance of humidity sensor
	reshum = val1 * 1e6 / (1024 - val1)
	val1hum = math.log10(reshum) * -105 / 13 + 105 + (temp / 20)

	# Determine humidity based on val2 reading
	# Find resistance of humidity sensor
	reshum = val2 * 1e6 / (1024 - val2)
	val2hum = (math.log10(reshum)-2) * -105 / 13 + 105 + (temp / 20)

	# Compare and pick appropriate value
	if (val2hum > 50 and val1hum > 50):
		# High humidity, return value 2
		return val2hum

	else:
		# Low humidity, return value 1
		return val1hum

# Convert ADC soil moisture reading to percent
def adc2soilmoist(val):

	# val = value of soil moisture sensor

	if (val < 0 or val > 1023):
		return -1


	soil = int(val * 100 / -700 + 800 / 7)
	

	if (soil < 0): soil = 0
	if (soil > 100): soil = 100


	return soil



