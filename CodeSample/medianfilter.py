import numpy as np
import time

class MedianFilter:

    def __init__(self, N, D):
        self.N = N;  #Dimension of input/output
        self.D = D;  #Number of previous scans used to calculate median
        self.counter = 0; #Used to keep track of D scans
        self.inputlist = [[] for x in xrange(D+1)]
                
    def update(self, inputArray):
	
	#Replaces oldest scan in the list of D scans
        if(self.counter>self.D):
            self.counter = 0
        self.inputlist[self.counter] = inputArray
        
	#Stores values from inputList(previous D scans) 
        calc_medianlist = [[] for x in xrange(self.N)]
        for x in self.inputlist:
            for index, item in enumerate(x):
                calc_medianlist[index].append(item)

        #Calculates Median
        print "Calculating Median using previous {0} scans or all scans so far".format(self.D)
        medianlist = []
        for x in calc_medianlist:
            medianlist.append(np.median(x))

        medianlist = np.asfarray(medianlist)
        self.counter += 1;
        return medianlist
           
        
        








        
    
