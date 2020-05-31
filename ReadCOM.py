import sys
import serial

ser1 = serial.Serial(port=sys.argv[1],baudrate=int(sys.argv[2])
ser2 = serial.Serial(port=sys.argv[1],baudrate=int(sys.argv[2]))
while True:  # The program never ends... will be killed when master is over.
    # sys.stdin.readline()

    #ser.write('serial command here\n') # send command to serial port
    output1 = ser1.readline() # read output
    output2 = ser2.readline()
    input1 = ser1.writeline() # read output
    input2 = ser2.writeline()
 
    sys.stdout.write(output1) # write output to stdout
    sys.stdout.flush()
    sys.stdout.write(output2) # write output to stdout
    sys.stdout.flush()
