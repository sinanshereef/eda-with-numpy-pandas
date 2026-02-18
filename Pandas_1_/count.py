
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']


# b=a.groupby('prof') ['prof'].count()
# c=a.groupby('location') ['location'].count() \
#     .sort_values(ascending=False)
# print(b)
# print(c)

# b=a.loc[a['location']=='india'] \
#     .groupby('prof') ['prof'].count() \
#     .sort_values(ascending=False)
# print(b)

b=a.loc[a['age']>40].groupby('location') ['location'].count() \
    .sort_values(ascending=False)
print(b)
print('*'*100)
c=a.loc[(a['age']>=25) & (a['age']<=40)] \
    .groupby('prof') ['prof'].count() \
    .sort_values(ascending=False)
print(c)


