import serial
from time import sleep
ser = serial.Serial('/dev/ttyUSB1', timeout=1)
ser.baudrate = 115200

msg = 'test'
ser.write(msg)
sleep(0.5)
ser.readline()
