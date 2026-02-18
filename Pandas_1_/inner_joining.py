import numpy as np
import pandas as pd
a=pd.DataFrame([[101,'Sinan','Shereef',23],
                [102,'Deepak','Prakash',21],
                [230,'jo','p',40],
                [370,'mike','k',34]])
a.columns=['id','fname','lname','age']
b=pd.DataFrame([['Engineer',230,'EKM',200],
                ['bigdata',101,'TVM',400],
                ['testing',102,'klm',234],
                ['python',370,'ktym',324]])
b.columns=['prof','id','location','salary']
print(a)
print('*'*100)
print(b)
print('*'*100)

c=pd.merge(a,b,on='id',how='inner')
print(c)
d=pd.merge(a,b,on='id',how='inner').loc[b['prof']=='bigdata'] [['fname','lname','age']]
print(d)
print('*'*100)
e=pd.merge(a,b,on='id').sort_values(by='age',ascending=False) [['fname','lname','age','prof','salary']] \
    .head(1)
print(e)
