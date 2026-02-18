
#loc is used to filter(satisfy a given condition)

#syntax---

#newdframe=olddframe.loc[oldframe['colmnname']condition]

#conditions are: <,>,<=,>=.==

# priority: loc column head/tail


import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/sample4.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','phone_number','location']
# df1=a[['fname','lname','age']].tail(2)  #last two emp of their fname,lname and age
# print(df1)

# df1=a.loc[a['age']>23]
# print(df1)
#
# b=a.loc[a['age']==21] [['fname','lname','age','phone_number']]
# print(b)

c=a.loc[a['age']<23] [['fname','lname','age','phone_number']]
print(c)

d=a.loc[a['location']=='Chennai'] [['fname','lname','age','phone_number']]
print(d)

e = a.loc[(a['age'] > 23) & (a['location'] == 'Chennai')] [['fname', 'lname', 'age', 'phone_number']]
print(e)