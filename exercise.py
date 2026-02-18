
# Question........
#1 to 50 element
#odd numbers==>2d[5,5]

import numpy as np

a=np.arange(1,51)
b=a%2!=0
c=a[b]
d=c.reshape(5,5)
print(d)