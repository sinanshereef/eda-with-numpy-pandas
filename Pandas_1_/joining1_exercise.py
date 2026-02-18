
import numpy as np
import pandas as pd
a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/custom_windows.csv",sep=',')
b=pd.read_csv("C:/Users/zinan/OneDrive/Documents/order_windows.csv",sep=',')
c=pd.merge(a,b,on='id',how='inner')
print(c)
print('*'*100)
d=c.sort_values(by='age',ascending=False) [['name','age','location','dat','amount']] \
    .head(1)
print(d)
print('*'*100)
e=c.sort_values(by='dat',ascending=False) [['name','age','location','dat','amount']] \
    .head(1)
print(e)