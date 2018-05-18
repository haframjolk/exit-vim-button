#!/usr/bin/env python3
import serial
import time
"""
Exit Vim Button
by Reynir Aron
Serial input handler
"""

serial_port = "/dev/cu.usbmodem1411441"
baud = 9600

arduino = serial.Serial(serial_port, baud, timeout=5)
time.sleep(2)

while True:
    msg = arduino.read(arduino.inWaiting())
    print(msg)

exit()
