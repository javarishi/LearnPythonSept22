import numpy as np

a = np.array([1,2,3,4])
print(a, type(a))
a = np.array([[1, 2], [3, 4]])
print(a)

a = np.array([[[1, 2], [3, 4]], [[5,6], [7,8]]])
print(a)

a = np.array([1, 2, 3,4,5], ndmin = 2)
print(a)

percentile = np.array([98,99,97,95,88,90], dtype=complex)
print(percentile)