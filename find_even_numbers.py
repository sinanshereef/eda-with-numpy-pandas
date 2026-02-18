
import numpy as np

a=np.array([3,0,5,8,6,4,9,2,1,7,11,100,25])
b=a%2==0
c=a[b]
print(c)