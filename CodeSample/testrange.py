import numpy as np
import rangefilter as rf
import time


range_min = input("Please enter the range minimum: ")
range_max = input("Please enter the range maximum: ")

print("Creating Range Filter......")
rangefilt = rf.RangeFilter(range_min, range_max)

sampleArray = np.arange(-25.0,100.0,0.1)
num_test_inputs = input("Please enter how many random inputs you wish to send to the filter: ")
N = input("Please enter the dimension(length) of the random inputs: ")

inputlist = [[] for x in xrange(num_test_inputs)]
for x in xrange(num_test_inputs):
    inputlist[x] = np.random.choice(sampleArray,N,replace=True)

for x in xrange(num_test_inputs):
    print "Input: {0}".format(inputlist[x])
    time.sleep(1.5)
    result = rangefilt.update(inputlist[x])
    print "Output: {0}".format(result)
    time.sleep(1.5)








