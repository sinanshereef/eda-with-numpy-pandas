
import numpy as np

a=np.array([3,2,7,9,5,8,5,3,1,0,2])

b=np.array_split(a,4)
print(b)
print(b[1])