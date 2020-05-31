import sys

counter = 0
while True:  # The program never ends... will be killed when master is over.
    counter += 1
    sys.stdin.readline()
    sys.stdout.write('Serial from com1 is %d\n' % counter)
    sys.stdout.flush()
