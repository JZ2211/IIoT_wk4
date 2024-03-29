# Demo: 
# Interface a thermocouple via MCP9600 with a Raspberry Pi
#
# Created 5/24/2023
# By Jin Zhu

import time
from datetime import datetime
import re
import sys
import board
import busio
from adafruit_mcp9600 import MCP9600

#MCP9600 setup
i2cbus = busio.I2C(board.SCL, board.SDA, frequency=100000 ) 
#use default raspberry pi board SCL and SDA for I2C, set frequency is required for MCP9600 board
#The default I2C address is 0x67 for adafruit MCP9600 board. range: 0x60-67
#Indicate the thermocouple used is K type. The default type is K and other
#options are 'J','T','N','S','E','B' or 'R'
thmcp = MCP9600(i2cbus,0x67, 'K')

datatype = "Date, Time, Thermocouple K type(@0x67) Temperature(C)"
try: 
     print("Start reading data from termocouple ......\n")
     print(datatype)
     while True:
      timestamp = str(datetime.now()) #obtain current time
     
      #thermocouple result
      typeK_temperature = thmcp.temperature #obtain the ambient temprature in Celsius degree

      timestamp = re.sub(' ',', ', timestamp)
      output = timestamp + ", {0:.1f}".format(typeK_temperature)

      print(output)  #display results in the terminal
      time.sleep(2) #data are collected roughly every 2 second

except KeyboardInterrupt:
      print("Interrupted by User")
      sys.exit(0)
