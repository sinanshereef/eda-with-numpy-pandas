
import numpy as np
import pandas as pd

dic={'name':'Sinan','age':23,'location':'Mannar','pincode':689622}
a=pd.Series(dic,index=['name','pincode','age','location'])
print(a)
