
import numpy as np

a=np.array([[1,2,3,6],[4,5,7,8]])
b=np.reshape(a,(4,2))
print(b)
print(b.ndim)

c=b.flatten()
print(c)

d=np.arange(1,21)
print(d)

e=np.linspace(1,100,5)
print(e)