import sys
import serial

ser = serial.Serial(port=sys.argv[1],baudrate=int(sys.argv[2]))
for _ in xrange(10)    # sys.stdin.readline()

    ser.write('serial command here\n') # send command to serial port
    output = ser.readline() # read output

    sys.stdout.write(output) # write output to stdout
    sys.stdout.flush()
    ser.close()
