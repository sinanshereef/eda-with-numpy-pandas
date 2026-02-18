
import numpy as np
import pandas as pd

lst=[200,400,300,800,1000,700,100,340,965,777]
a=pd.Series(lst)
b=pd.Series([1,2,3,4,5,6,7,8,9,0])

c=a._append(b,ignore_index=True)
print(c)