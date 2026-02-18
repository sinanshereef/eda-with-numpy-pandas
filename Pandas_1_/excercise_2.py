
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']
print(a)

print('*'*100)
#1. age above 50 fname,lname,age,prof
b=a.loc[a['age']>50] \
    [['fname','lname','age','prof']]
print(b)
# 2. age 25-40 fname,lname,age,prof
c = a.loc[(a['age'] >= 25) & (a['age'] <= 40)] \
    [['fname', 'lname', 'age', 'prof']]
print(c)
#3. india work fname,lname,age,prof
d=a.loc[a['location']=='india'] \
    [['fname', 'lname', 'age', 'prof']]
print(d)
#4. india work and age above 50 fname,lname,age,prof
e=a.loc[(a['location']=='india') & (a['age']>50)] \
    [['fname', 'lname', 'age', 'prof']]
print(e)
#5. age max 10 employee fname,lname,age,prof
f=a.sort_values(by='age',ascending=False) \
    [['fname', 'lname', 'age', 'prof']] \
    .head(10)
print(f)
#6. age min 6 employee fname,lname,age,prof
g=a.sort_values(by='age') \
    [['fname', 'lname', 'age', 'prof']] \
    .head(6)
print(g)
#7. uk work and age below 40 fname,lname,age
h=a.loc[(a['location']=='uk') & (a['age']<40)] \
    [['fname', 'lname', 'age', 'prof']]
print(h)
#8. india work and prof doctor fname,lname,age
i=a.loc[(a['location']=='india') & (a['prof']=='doctor')] \
    [['fname', 'lname', 'age']]
print(i)
#9. india work age max 3 employee fname,lname,age,prof
j=a.loc[(a['location']=='india')] \
    .sort_values(by='age',ascending=False) \
    .head(3)
print(j)
#10. india work age min 2 employee fname,lname,age
k=a.loc[(a['location']=='india')] \
    .sort_values(by='age') \
    .head(3)
print(k)
#11. india work and prof doctor,age min 1 employee
# fname,lname,age
l=a.loc[(a['location']=='india')&(a['prof']=='doctor')] \
    .sort_values(by='age') \
    [['fname', 'lname', 'age']] \
    .head(1)
print(l)
#12. pilot prof,age max 2 employee fname,lname,age
m=a.loc[a['prof']=='pilot'] \
    .sort_values(by='age',ascending=False) \
    [['fname', 'lname', 'age', 'prof']] \
    .head(2)
print(m)
#13. pilot prof,age min 1 employee full details
n=a.loc[a['prof']=='pilot'] \
    .sort_values(by='age') \
    .head(1)
print(n)