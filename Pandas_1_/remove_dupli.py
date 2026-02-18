
import numpy as np

import pandas as pd

lst=[[101,'Sinan','Shereef',23,'Engineer',100000,'Thiruvalla'],
     [102,'Deepak','Prakash',20,'Engineer',100000,'kollam'],
     [103,'Jithu','Philip',21,'Data Scientist',100000,'Pathanamthitta'],
     [104,'Vinay','bro',20,'Developer',100000,'kannur'],
     [105,'Sangeeth','bro',20,'Proffessor',20000,'kannur'],
     [106,'Aditya','Kottayam',22,'Dentist',300,'kottayam'],
     [107,'Sethulekshmi','vinod',20,'Teacher',8990,'Alappuzha'],
     [104,'Vinay','bro',20,'Developer',100000,'kannur'],
     [102,'Deepak','Prakash',20,'Engineer',100000,'kollam'],
     [101,'Sinan','Shereef',23,'Engineer',100000,'Thiruvalla']]

df=pd.DataFrame(lst)
df.columns=['id','F_name','L_name','Age','Prof','Salary','location']
df1=df.drop_duplicates()
print(df1)