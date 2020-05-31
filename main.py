from subprocess import Popen, PIPE
p1 = Popen(['python', './ReadCOM.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE) # read COM1 permanently

finished = False
while not finished:
    print "received from COM1: %s" % p1.stdout.readline() # print output from ReadCOM.py for COM1
