class RangeFilter:

    def __init__(self, range_min, range_max):
        self.range_min = range_min
        self.range_max = range_max
   
    
    def update(self, inputArray):

        filteredArray = inputArray

        for index, item in enumerate(inputArray):
            if(item < self.range_min):
                filteredArray[index] = self.range_min
            elif(item > self.range_max):
                filteredArray[index] = self.range_max
            else:
                filteredArray[index] = item;
        
        return filteredArray


