"""Setup serial communication between Lopy, Arduino and PC.
Disable LED.
"""
import os
import machine
import pycom


# Configure first UART bus to see the communication on the pc
uart = machine.UART(0, 115200)
os.dupterm(uart)

# Configure second UART bus on pins P3(TX1) and P4(RX1)
uart1 = machine.UART(1, baudrate=9600)

pycom.heartbeat(False)

machine.main('main.py')
print('==========Starting main.py==========\n')
