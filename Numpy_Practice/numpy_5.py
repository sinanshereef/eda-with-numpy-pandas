
import numpy as np

df=np.array([2,3,6,84,32,1,3,5,1])
c=np.sum(df)
print(c)

d=np.max(df)
print(d)

e=np.min(df)
print(e)

e=np.sort(df)
print(e)

f=np.sort(df)[::-1]
print(f)

g=np.sort(df,axis=0)
print(g)
