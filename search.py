
import numpy as np

a=np.array([3,2,7,9,5,8,5,3,1,0,2,10,7,2,90,200])

b=np.where(a==3)
print(b)

c=np.where(a==200)
print(c)

d=np.where(a>10)
print(d)

