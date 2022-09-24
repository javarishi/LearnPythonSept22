import numpy as np
x = np.arange(10,20,2)
print(x)
x = np.linspace(10,20,5) # linspace includes end point
print(x)
x = np.linspace(10,20,5, endpoint=False) # linspace includes end point - if u dont want then use endpoint=False
print(x)

a = np.arange(10)
s = slice(2,7,2)
print(a[s])

a = np.arange(10)
b = a[2:7:2]
print(b)

import numpy as np
a = np.arange(10)
print(a[5:])
print(a[:5])
