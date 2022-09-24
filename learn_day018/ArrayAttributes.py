import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print (a.shape)
b = a.reshape(3,2)
print (b)
# arange - start, end, step - exactly same as for loop range function
a = np.arange(24)
print(a)
print (a.itemsize)
b = a.reshape(2,4,3)
print(b)
