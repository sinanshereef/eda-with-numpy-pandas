
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']
b=a.groupby('prof') ['age'].max()
print(b)
print('*'*100)
c=a.groupby('location') ['age'].max()
print(c)
print('*'*100)

d=a.loc[a['location']=='india'] \
    .groupby('prof') ['age'].max() \
    .sort_values(ascending=False)
print(d)