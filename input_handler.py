#!/usr/bin/env python3
import serial
import time
import subprocess
"""
Exit Vim Button
by Reynir Aron
Serial input handler
"""
serial_port = "/dev/cu.usbmodem1411441"
baud = 9600
signal = "1"  # Signal sent by Arduino

try:
    arduino = serial.Serial(serial_port, baud, timeout=5)
    time.sleep(2)  # Give serial monitor 2 seconds to connect

    while True:
        msg = arduino.readline().decode("utf-8")
        if msg.rstrip() == signal:
            print("Signal received.")
            subprocess.call(["osascript", "exit_vim.scpt"])

except KeyboardInterrupt:
    print("Shutdown requested. Exiting...")
    exit(0)
