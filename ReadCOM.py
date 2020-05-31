import sys
import serial

ser1 = serial.Serial("/dev/ttyUSB0", "115200")
while True:  # The program never ends... will be killed when master is over.
    # sys.stdin.readline()

    ser1.write(output2) # send command to serial port
    output1 = ser.readline() # read output

    sys.stdout.write(output1) # write output to stdout
    sys.stdout.flush()
    
ser2 = serial.Serial("/dev/ttyUSB1", "115200")
while True:  # The program never ends... will be killed when master is over.
    # sys.stdin.readline()

    ser2.write(output1) # send command to serial port
    output2 = ser.readline() # read output

    sys2.stdout.write(output2) # write output to stdout
    sys2.stdout.flush()
