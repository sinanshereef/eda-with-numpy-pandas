
import numpy as np

buff=np.array([4,3,2,2,32,3,3,4,2,3,445,6,2])
c=np.array_split(buff,2)
print(c)

suf=np.array([3,4,2,5,7,8,90,8,7,67,11,412,56])
d=np.concatenate([buff,suf])
print(d)

