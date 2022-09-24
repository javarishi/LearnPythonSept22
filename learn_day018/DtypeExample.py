import numpy as np

age = np.dtype(np.float64)
# i1 = int8, i2 = int16, i4 = int32, i8=int64
# S20 - 20 character string
a = np.array([1,2,3,4,5], 'i4')
print(a)

age_dt = np.dtype([('age', np.int8)])
dataset = [(10,),(20,),(30,)]
age_array = np.array(dataset, age_dt)
print(age_array)

student_dt = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
dataset = [('David', 10, 88),('Neil' , 12, 90),("Byron", 11, 91)]
student_array = np.array(dataset, student_dt)
print(student_array)