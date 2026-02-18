
import numpy as np
import pandas as pd

dic={'name':'Sinan','age':23,'location':'Mannar','pincode':689622}
a=pd.Series(dic)
print(a)
print(a.head(2))
print(a.tail(2))
print(a.dtype)