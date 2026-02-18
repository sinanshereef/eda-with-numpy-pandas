import numpy as np

a=np.array([[1,2,3],[2,3,4],[4,5,6]])
b=np.array([[0,9,8],[7,6,5],[9,5,2]])

c=np.concatenate([a,b])
print(c)  #default=column-wise

d=np.concatenate([a,b],axis=1)
print(d) #row-wise