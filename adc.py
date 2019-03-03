# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import datetime
import dataProcess

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#to read ADC
#var = mcp.read_adc(channel_num)

while True:

	
	light = adc2light(mcp.read_adc(0))
	humid = adc2humidity(mcp.read_adc(1), mcp.read_adc(2), 25)
	soil = adc2soilmoist(mcp.read_adc(3))

	curr = datetime.datetime.now()

	datestring = str(curr)


	print light, ", ", humid, ", ", soil
