
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/heart.csv",sep=',')

# #Find total no:of rows
# print(a.shape[0])
#
# #print column names
# for i in a:
#     print(i)
#
# #print 1st 5 rows
# c=a.iloc[:5,:]
# print(c)

# #last 5 rows
# d=a.iloc[-5:,:]
# print(d)

# #print data-types
# print(a.dtypes)

#find target column count
# c=a.groupby('target') ['target'].count()
# print(c)

# # #find total number of missing values
print(a.isna().sum())

#fill the missing values in a proper method
x=a['trestbps'].mode()[0]
a['trestbps'].fillna(x,inplace=True)
print(a)
y=a['restecg'].mode()[0]
a['restecg'].fillna(y,inplace=True)
print(a)
z=a['thalach'].mode()[0]
a['thalach'].fillna(z,inplace=True)
print(a)
l=a['ca'].mode()[0]
a['ca'].fillna(l,inplace=True)
print(a)
r=a['thal'].mean()
a['thal'].fillna(r,inplace=True)
print(a)
print(a.isna().sum())
g=a['trestbps'].mean()
for i in a.index:
    if a.loc[i,'trestbps']>=170:
        a.loc[i,'trestbps']=g
print(a)

a.to_csv("C:/Users/zinan/OneDrive/Documents/heart_cleaning.csv",index=False)