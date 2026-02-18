

import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']
#1. Find Row count
print(a.shape[0])
print('*'*100)
#2. Remove duplicates rows and find total row count
b=a.drop_duplicates()
print(b.shape[0])
print('*'*100)
#3. Age maximum 10 fname,lname,prof,loc
c=a.sort_values(by='age',ascending=False) [['fname','lname','age','prof','location']].head(10)
print(c)
print('*'*100)
#4. Age minimum 5 employees fname,lname,prof,loc
d=a.sort_values(by='age') [['fname','lname','age','prof','location']].head(5)
print(d)
print('*'*100)
# 5. Each location count  [count desc order]
e=a.groupby('location') ['location'].count() \
    .sort_values(ascending=False)
print(e)
print('*'*100)
# 6. Full data
f=a.loc[a['location']=='australia'] [:]
print(f)
print('*'*100)
# 7. Each age group count [age desc order]
g=a.groupby('age') ['age'].count() \
    .sort_values(ascending=False)
print(g)
print('*'*100)
# 8. Each profession count [count desc order]
h=a.groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(h)
print('*'*100)
print('*'*100)
print('*'*100)
# 9. India work
# A. Row count
i=a.loc[a['location']=='india']
print(i.shape[0])
print('*'*100)
# B. Each profession count [count desc order]
j=a.loc[a['location']=='india'].groupby('prof') ['prof'] \
    .count().sort_values(ascending=False)
print(j)
print('*'*100)
# C. Age mxm 3 employees fname,lname,age,prof
k=a.loc[a['location']=='india'].sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(3)
print(k)
print('*'*100)
# D. Age minimum 3 employees fname,lname,age,prof
l=a.loc[a['location']=='india'].sort_values(by='age') [['fname','lname','age','prof']].head(3)
print(l)
print('*'*100)
# age above 40 full data
m=a.loc[(a['location']=='india') & (a['age']>40)] [:]
print(m)
print('*'*100)
# F. age range 30 to 40 [profession count]
n=a.loc[(a['location']=='india') & ((a['age']>=30) & (a['age']<=40))] [:]
print(n)
print('*'*100)
print('*'*100)
# 10. us work
# A. Row count
o=a.loc[a['location']=='uk'].shape[0]
print(o)
print('*'*100)
# B. Each age group count
p=a.loc[a['location']=='uk'].groupby('age') ['age'].count()
print(p)
print('*'*100)
# C. Each profession count  [count desc]
q=a.loc[a['location']=='uk'].groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(q)
print('*'*100)
# D. Civil engineer dept and age above 30
r=a.loc[(a['location']=='uk') & ((a['prof']=='Civil engineer') & (a['age']>30))]
print(r)