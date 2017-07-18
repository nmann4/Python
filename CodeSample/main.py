import numpy as np

range_min = 0.03
range_max = 50.0

sampleArray = np.arange(0.0,100.1,0.1)
randArray = np.random.choice(sampleArray,200,replace=True)

#resultArray = [x if (x < range_max) else range_max for x in randArray]

resultArray = randArray

for index, item in enumerate(randArray):
    if(item < range_min):
        resultArray[index] = range_min
    elif(item > range_max):
        resultArray[index] = range_max
    else:
        resultArray[index] = item;

#resultArray = np.asfarray(resultArray)
print resultArray

