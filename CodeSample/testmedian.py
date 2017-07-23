import numpy as np
import medianfilter as mf
import time

D = input("Please Enter D parameter (# Scans used to calculate Median) for medianfilter: ")
N = input("Please Enter N parameter (Dimension of I/O) for medianfilter: ")
print "Creating temporal median filter"
medianfilt = mf.MedianFilter(N, D)

#Sample size for random arrays
sampleArray = np.arange(0.0,11.0,1.0) 

num_test_inputs = input("Please enter how many random inputs you " \
			"wish to send into filter: ")

#Creates random input
inputLists = [[] for x in xrange(num_test_inputs)]
for x in xrange(num_test_inputs):
    inputLists[x] = np.random.choice(sampleArray,N,replace=True)

#Filters input Data
for x in xrange(num_test_inputs):
    print "INCOMING LIDAR SCAN"
    time.sleep(1)
    print "Input: {0}".format(inputLists[x])
    time.sleep(1)
    result = medianfilt.update(inputLists[x])
    time.sleep(1)
    print "Output: {0}".format(result)
    time.sleep(1) 




