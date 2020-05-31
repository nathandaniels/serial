from subprocess import Popen, PIPE

# call subprocess
# pass the serial object to subprocess
# read out serial port


# HOW TO PASS SERIAL OBJECT HERE to stdin
p1 = Popen(['python', './ReadCOM.py', "/dev/ttyUSB0", "115200"], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM1 permanently
p2 = Popen(['python', './ReadCOM.py', "/dev/ttyUSB1", "115200"], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM2 permanently

finished = False
while not finished:
    print "received from COM1: %s" % p1.stdout.readline() # print output from ReadCOM.py for COM1
    print "received from COM2: %s" % p2.stdout.readline() # print output from ReadCOM.py for COM2
    
    ser1 = serial.Serial('/dev/ttyUSB0', 115200, timeout=0.5)
    ser1.write(p2.stdout.readline())
    time.sleep(0.1)
    ser1.close()
    
    see2 = serial.Serial('/dev/ttyUSB1', 115200, timeout=0.5)
    ser2.write(p1.stdout.readline())
    time.sleep(0.1)
    ser2.close()
