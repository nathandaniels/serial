import serial
ser1 = serial.Serial('/dev/ttyUSB0')
ser1.baudrate = 115200
ser2 = serial.Serial('/dev/ttyUSB1')
ser2.baudrate = 115200
while True:
  output1 = ser1.readline()
  output2 = ser2.readline()
  ser1.write(output2)
  ser2.write(output1)
  
