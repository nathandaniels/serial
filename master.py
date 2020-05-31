from subprocess import Popen, PIPE
from time import sleep

p = Popen(['python', './com.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
print "serial communication started."  # com.py is working but we moved on!
for i in range(3):
    p.stdin.write('<command-here>\n')
    print "comand sent."
    print "received : %s" % p.stdout.readline()
    sleep(1)
