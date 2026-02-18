

import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/sample4.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','phone_number','location']
b=a.sort_values(by='age',ascending=False) \
    [['fname','lname','age','phone_number']] \
    .head(2)
print(b)
print('*'*100)
c=a.sort_values(by='age') \
    [['fname','lname','age','phone_number']] \
    .head(1)
print(c)
print('*'*100)
d=a.loc[a['location']=='Chennai'] \
    .sort_values(by='age',ascending=False) \
    [['fname','lname','age','phone_number']] \
    .head(1)
print(d)
