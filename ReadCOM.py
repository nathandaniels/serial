import sys
import serial

ser1 = serial.Serial("/dev/ttyUSB0", "115200")
ser2 = serial.Serial("/dev/ttyUSB1", "115200")
while True: 
    output1 = ser1.readline()
    output2 = ser2.readline()
    ser1.write(output2)
    ser2.write(output1)
    sys.stdout.write(output2)
    sys.stdout.write(output1)
    sys.stdout.flush()
   
