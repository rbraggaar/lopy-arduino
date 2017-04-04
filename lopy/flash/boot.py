"""Enable serial communication with the Lopy.
Disable LED.
"""
import os

import pycom
import machine
from network import WLAN

# Configure first UART bus to see the communication on the pc
uart = machine.UART(0, 115200)
os.dupterm(uart)
# Configure second UART bus on pins P3(TX1) and P4(RX1)
uart1 = UART(1, baudrate=9600)

wl = WLAN()

pycom.heartbeat(False)

machine.main('main.py')
print('==========Starting main.py==========\n')

