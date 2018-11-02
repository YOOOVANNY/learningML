import numpy as np
from numpy import pi

#np.array is used to make an array
a = np.array([2, 3, 4])
print(a)
print(a.dtype)

#can also be used to create a multidimensional array
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print(b.dtype)

#you can specify the type of data stored in the array at creation time
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

#np.zeros is used to make an array of given dimension filled with zeros
print(np.zeros((3, 4)))

#np.ones
print(np.ones((2, 3, 4), dtype=np.int16))

#np.empty is uninitialized and can output random information
print(np.empty((2, 3)))

#np.arange creates a list in a certain range at certain increments (start, stop, increments), includes the start value but doesn't include the stop value
print(np.arange(10, 30, 5))
#accepts float arguments
print(np.arange(0, 2, 0.3))

#np.linspace uses the argument to show how many we want and not how many to increment by
print(np.linspace(0, 2, 9)) #9 numbers between 0 and 2

x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)
print(x)
print(f)

print(np.arange(10000).reshape(100,100))