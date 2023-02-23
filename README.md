# Air Mouse Using Arduino and MPU6050
## Circuit Diagram:
  
## Overview:
This program was written as an alternative for the Arduino Leonardo and MPU6050 based gesture mouse projects
as Arduino Uno or Nano(the ones which I own) are not compatible with the Mouse.h library because they are not 
32u4 or SAMD micro based boards.

The code simply corrects and processes the data from MPU6050 and sends it to your computer via serial communication.
The Python script reads the data and moves the mouse reletive to the angle of tilt of the sensonr. 
The Mouse Enable button is to be pushed when you want the mouse to move. 
To recalibrate the gyro, just press the reset button on your Arduino. Some notable changes were made to the MPU6050_tockn.h 
to optimise the code but you can leave it as it is.Results may vary. 
There is some latency involved, I guess its due to the library but I'm not sure, feel free to bind this
approach with other MPU6050 libraries.
    
## Prerequisites:
**Software :**
* Arduino IDE
* MPU6050 Library from https://github.com/tockn/MPU6050_tockn
* Python 3
* pynput Python library (pip install pynput)
* 
**Hardware :**
* Arduino Uno or Nano or any ATMEGA328 based board (or ESP32 for Blutooth Capabilities)
* MPU6050 Gyro Sensor
* Three 10KΩ Resistors
* Three push to on buttons
