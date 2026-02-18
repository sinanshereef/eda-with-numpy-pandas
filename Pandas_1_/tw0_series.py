
import numpy as np
import pandas as pd

lst=[200,400,300,800,1000,700,100,340,965,777]
a=pd.Series(lst)
b=pd.Series([1,2,3,4,5,6,7,8,9,0])

c=a.add(b)
print(c)

d=a.subtract(b)
print(d)

e=a.multiply(b)
print(d)

f=a.div(b)
print(f)