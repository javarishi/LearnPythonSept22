# convert list to ndarray
import numpy as np
x = [1,2,3]
a = np.asarray(x)
print(a)
x = (1,2,3)
a = np.asarray(x)
print(a)
list_of_tuple = [(1,2,3), (5,6,7)]
a = np.asarray(list_of_tuple)
print(a)