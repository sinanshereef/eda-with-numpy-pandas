
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/movies.csv",sep=',',header=None)
a.columns=['id','name','year','rating','duration']

# 1. Find row count
print(a.shape[0])
print('*'*100)
# 2. Remove duplicates and find row count
b=a.drop_duplicates().shape[0]
print(b)
print('*'*100)
# 3. Sort data set by release year in des order
c=a.sort_values(by='year',ascending=False)
print(c)
print('*'*100)
# 4. Find rating mxm 5 movies name,year,rating
d=a.sort_values(by='rating',ascending=False) [['name','year','rating']] \
    .head(5)
print(d)
print('*'*100)
# 5. Find rating minimum 3 movies name,year,rtaing
e=a.sort_values(by='rating') [['name','year','rating']] \
    .head(3)
print(e)
print('*'*100)
# 6. Find Each year release movie count [count desc order]
f=a.groupby('year') ['year'].count() \
    .sort_values(ascending=False)
print(f)
print('*'*100)
# 7. Each rating count [count desc order]
g=a.groupby('rating') ['rating'].count() \
    .sort_values(ascending=False)
print(g)
print('*'*100)
# 8. 2008 and rating above 3 [collect]
# A. row count
h=a.loc[(a['year']==2008) & (a['rating']>3)].shape[0]
print(h)
print('*'*100)
# 9. Find duration mxm 1 movies name,year,rating,duration
i=a.sort_values(by='duration',ascending=False) [['name','year','rating','duration']] \
    .head(1)
print(i)
print('*'*100)
# 10. Find rating mnm 1 movies name,year,rating,duration
j=a.sort_values(by='rating') [['name','year','rating','duration']] \
    .head(1)
print(j)
print('*'*100)
# 11. Rating above 4 and relase year above 2005
# A. Rating mxm movies full data
k=a.loc[(a['rating']>4) & (a['year']>2005)].sort_values(by='rating',ascending=False).head(1)
print(k)
print('*'*100)
# B. Rating mnm movies full data
l=a.loc[(a['rating']>4) & (a['year']>2005)] \
    .sort_values(by='rating').head(1)
print(l)
print('*'*100)
# 12. 2008 movies count
m=a.loc[a['year']==2008] \
    .groupby('year') ['year'] \
    .count()
print(m)
print('*'*100)
# 13. 1975-2000 movies collect
# A. Row count
n=a.loc[(a['year']>=1975) & (a['year']<=2000)].shape[0]
print(n)
print('*'*100)
# 14. 1975-2000 and rating above 3.5 total row count
o=a.loc[((a['year']>=1975) & (a['year']<=2000)) & (a['rating']>3.5)].shape[0]
print(o)