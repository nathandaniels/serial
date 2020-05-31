import serial

serialport0 = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)
serialport1 = serial.Serial("/dev/ttyUSB1", 115200, timeout=0.5)

while True:    
    command0 = serialport0.read()
    print str(command0)
    seriaport1.write(command0.encode())
    command1 = serialport1.read()
    print (str(command1)
    seriaport0.write(command1.encode())

