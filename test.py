import serial

serialportzero = serial.Serial("/dev/ttyUSB0", 115200, timeout=0.5)
serialportone = serial.Serial("/dev/ttyUSB1", 115200, timeout=0.5)

while True:    
    commandzero = serialportzero.read()
    print str(commandzero)
    serialportone.write(commandzero.encode())
    commandone = serialportone.read()
    print str(commandone)
    serialportzero.write(commandone.encode())

