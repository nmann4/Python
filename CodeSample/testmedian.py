import numpy as np


inputLists = [[] for x in xrange(3)]
inputLists[0] = [0.,1.,2.,1.,3.]
inputLists[1] = [1.,5.,7.,1.,3.]
inputLists[2] = [2.,3.,4.,1.,0.]

calcmedianLists = [[] for x in xrange(5)]

for x in inputLists:
    for index, item in enumerate(x):
        calcmedianLists[index].append(item)

print "Calculating Median"
medianList = []

for x in calcmedianLists:
    medianList.append(np.median(x))

print "Medians after update are: "
medianList = np.asfarray(medianList)
print medianList
