import os
import re
import subprocess
import atexit

os.system('python3 googler')

cmd = "wc -l < cmd.LOG | bc"

# count number of errors in error.LOG
errors = 0
array = []
try:
    fp = open('error.LOG', 'r')
    for line in fp:
        if re.match('(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}),(\d{3}) : (.*)', line):
            errors += 1
            array.append(line)
finally:
    fp.close()
    print (errors)

# perform on exit
def exit_handler():
    print ('=======================================')
    print ('LOGGER RESULTS')
    print ('=======================================')
    output = subprocess.getoutput(cmd)
    print ('Number of queries ran: ', int(output)-1)
    print ('Number of errors caught: ', errors)
    if errors > 10:
        print ('CAUTION: Number of errors encountered is fairly large (> 10)...')
    print ('\nShowing errors...')
    for i in array:
        print (i.strip('\n'))

atexit.register(exit_handler)
