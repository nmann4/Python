import numpy as np
import medianfilter as mf
import time

D = input("Please Enter D parameter for medianfilter: ")
N = input("Please Enter N parameter for medianfilter: ")
print "Creating temporal median filter\n"
medianfilt = mf.MedianFilter(N, D)

#Sample size for random arrays
sampleArray = np.arange(0.0,11.0,1.0) 

num_test_inputs = input("Please enter how many random inputs you " \
			"wish to send into filter: ")

inputLists = [[] for x in xrange(num_test_inputs)]
for x in xrange(num_test_inputs):
    inputLists[x] = np.random.choice(sampleArray,N,replace=True)

for x in xrange(num_test_inputs):
    print "Input: {0}".format(inputLists[x])
    time.sleep(1.5)
    result = medianfilt.update(inputLists[x])
    time.sleep(1.5)
    print "Output: {0}".format(result)
    time.sleep(1.5) 




