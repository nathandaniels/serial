while True:
  p1 = Popen(['python', './ReadCOM.py', "/dev/ttyUSB0", "115200"], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM1 permanently
  p2 = Popen(['python', './ReadCOM.py', "/dev/ttyUSB1", "115200"], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM2 permanently
  print "received from COM1: %s" % p1.stdout.readline() # print output from ReadCOM.py for COM1
  print "received from COM2: %s" % p2.stdout.readline() #
  
