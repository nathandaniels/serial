import serial

ser1 = serial.Serial("/dev/ttyUSB0", "115200", timeout=1.0)
ser2 = serial.Serial("/dev/ttyUSB1", "115200", timeout=1.0)

while True: 
    output1 = ser1.readline()
    output2 = ser2.readline()
    ser1.write(output2)
    ser2.write(output1)
