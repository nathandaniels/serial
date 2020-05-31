import serial

serialport = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)

while True:    
    command = serialport.read()
    print str(command)
