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

try:
    arduino = serial.Serial(serial_port, baud, timeout=5)
    time.sleep(2)  # Give serial monitor 2 seconds to connect

    while True:
        msg = arduino.readline().decode("utf-8")
        print(msg, end="")
        if msg.rstrip() == "1":
            print()

except KeyboardInterrupt:
    print("Shutdown requested. Exiting...")
    exit(0)
