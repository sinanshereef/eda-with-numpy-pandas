

import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']


#iloc........


# df1=a.iloc[3:10,:4]
# print(df1)

x=a.iloc[:,:-1]
print(x)

y=a.iloc[:,-1]
print(y)