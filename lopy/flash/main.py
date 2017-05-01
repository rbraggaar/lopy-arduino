"""Sends a string to the Arduino. Waits one second and then reads the answer
from the Arduino.
"""
import time


print('Main start')

while True:
    uart1.write('Hello Arduino')
    time.sleep(1)
    print(uart1.readline())  # read the response from the Arduino
    time.sleep(1)
