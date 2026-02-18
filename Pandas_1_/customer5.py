
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer5_windows.csv",sep=',')
#total row
print(a.shape[0])
print('*'*100)
#each prof count==>count desc
b=a.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(b)
print('*'*100)
#india,work each prof count==>count desc
c=a.loc[a['loc']=='india'] \
    .groupby('prof') ['prof'] \
    .count().sort_values(ascending=False)
print(c)
print('*'*100)
#Each prof,max_salary==>salary desc
d=a.groupby('prof') ['salary'].max() \
    .sort_values(ascending=False)
print(d)
print('*'*100)
#each location,min age==>age asc
e=a.groupby('loc') ['age'].min() \
    .sort_values()
print(e)
print('*'*100)
#each prof,total salary==>salary desc
f=a.groupby('prof') ['salary'].sum() \
    .sort_values(ascending=False)
print(f)
print('*'*100)
#india,each prof min age==>age desc
g=a.loc[a['loc']=='india'] \
    .groupby('prof') ['age'] \
    .min().sort_values(ascending=False)
print(g)
print('*'*100)
#us work,each prof avg sallary==>salary desc
h=a.loc[a['loc']=='us'] \
    .groupby('prof') ['salary'].mean() \
    .sort_values(ascending=False)
print(h)
print('*'*100)
#india work and age above 25,each prof avg salary
i=a.loc[(a['loc']=='india') & (a['age']>25)] \
    .groupby('prof') ['salary'].mean()
print(i)