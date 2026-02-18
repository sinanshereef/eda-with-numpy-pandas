
import numpy as np

a=np.array([1,2,3,4,5,6,7,8,9,0])

b=np.min(a)
print(b)

print("*"*100)
d=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])

c=np.min(d,axis=0)
print(c)