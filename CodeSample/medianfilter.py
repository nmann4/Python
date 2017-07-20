import numpy as np

class MedianFilter:

    def __init__(self, N, D):
        self.N = N;
        self.D = D;
        self.counter = 0;
        self.inputlist = [[] for x in xrange(D+1)]
                
    def update(self, inputArray):

        if(self.counter>self.D):
            self.counter = 0
        self.inputlist[self.counter] = inputArray
        
        calc_medianlist = [[] for x in xrange(self.N)]
    
        
        for x in self.inputlist:
            for index, item in enumerate(x):
                calc_medianlist[index].append(item)

        print "Calculating Median"
        medianlist = []

        for x in calc_medianlist:
            medianlist.append(np.median(x))

        print "Medians after update are: "
        medianlist = np.asfarray(medianlist)
        #print medianlist
        self.counter += 1;

        return medianlist
           
        
        








        
    
