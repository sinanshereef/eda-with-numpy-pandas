
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']
b=a.groupby('prof') ['age'].min()
print(b)
print('*'*100)
c=a.loc[a['location']=='us'] \
    .groupby('prof') ['age'].min() \
    .sort_values()
print(c)

#age(max)

d=a['age'].max()
print(d)
e=a['age'].min()
print(e)