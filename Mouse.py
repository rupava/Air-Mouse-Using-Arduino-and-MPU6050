# This Python code is an extension script for the Air Mouse using Arduino and MPU6050.
# Visit the Github page for the Arduino code and other information related to the project.
# https://github.com/rupava/Air-Mouse-Using-Arduino-and-MPU6050
# -By Rupava Baruah


import serial
from serial import Serial
from pynput.mouse import Button, Controller

mouse = Controller()
try:
  ser = serial.Serial('COM7',baudrate = 115200)       # Setting Serial port number and baudrate
  while 1:                                            # While loop to continuesly scan and read data from serial port and execute
      dump = ser.readline()                           # Reading Serial port
      dump = str(dump)                                # Converting byte data into string
      dump = dump[2:-5]                               # Cleaning up the raw data recieved from serial port
      data = dump.split(',')                          # Spliting up the data to individual items in a list. the first item being the data identifier
      print(data)
      if data[0] == "DATAL":                          # Checking if the identifier is "DATAL" which the Arduino sends the data as the gyro X, Y and Z values
        mouse.move(int(data[1]), int(data[2]))        # Moving the mouse by using the X and Y values after converting them into integer
        
      if data[0] == "DATAB":                          # Checking if the identifier is "DATAB" which the Arduino sends the values for Left/Right button
            if data[1] == 'L' :                       # If the Left button is pressed
              mouse.press(Button.left)                # The corresponding button is pressed and released
              mouse.release(Button.left)
            if data[1] == 'R' :                       # If the Right button is pressed
                    mouse.press(Button.right)         # The corresponding button is pressed and released
                    mouse.release(Button.right)
except:
  print("Mouse not found or disconnected.")
  k=input("Press any key to exit.")