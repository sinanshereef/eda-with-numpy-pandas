
import numpy as np

c=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])

d=np.sum(c,axis=0)
e=np.sum(c,axis=1)
print(d)
print(e)