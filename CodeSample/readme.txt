INTRODUCTION

	Hello Brain Corporation! First off I want to say thank you for the opportunity. I chose to create the the range filter and median filter in python. I do not think I would have completed the matrix library within a week as I have other coding challenges to do as well.


DOCUMENTATION
	
	RangeFilter
		Initialized with a range min and range max

		update(inputArray)
			Takes in an input array and returns a filtered array

	MedianFilter
		Initialized with parameters N (Dimension) and D (# Scans to calcualte median)

		update(inputArray)
			Takes in an input array and returns a filtered array

TESTING

	Testing was done by using the two main driver applications testrange.py and testmedian.py. If you wish to test simply run them from the terminal. At the moment they do not check for incorrect input.

	The range filter was tested by sending a random number of inputs that range from -25 to 100. If you wish to change the range of the random sample simply modify the line that creates the sampleArray. I understand negative values may not be common input but it allows us to see if filter is working correctly with a lower range minimum/higher range maximum.
	
	The median filter was tested by sending a random amount of inputs that ranges from 0 to 10. If you wish to change the range of the random sample simply modify the line that creates the sampleArray. The time delay was added to see that the object works correctly

Conclusion
	
	Overall I feel like I accomplished the task but there is always more functionality that can be added. I want to say that I treated this as a learning opportunity to learn more python as I have more years of experience in C++ than python.


References:

https://docs.python.org/3/tutorial/index.html
https://docs.scipy.org/doc/numpy/reference/index.html
https://stackoverflow.com/questions/5518435/python-fastest-way-to-create-a-list-of-n-lists
https://stackoverflow.com/questions/6340351/python-iterating-through-list-of-list
https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
