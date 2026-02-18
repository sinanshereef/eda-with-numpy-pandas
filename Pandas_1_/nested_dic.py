

import numpy as np
import pandas as pd

dic={'id':[1,2,3,4,5,6,7],'F_name':['Sinan','Vivek','Deepak','Anandhu','Shiva','George','Musa'],'L_name':['Shereef','Gopu','Roy','Madhu','Wick','lal','shibu'],'Age':[23,23,24,21,19,25,22],'Salary':[900,500,300,700,1000,350,600]}
df=pd.DataFrame(dic)
print(df)
print(df.ndim)
print(df.shape)
print(df.size)
print(df.dtypes)