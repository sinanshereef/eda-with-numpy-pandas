
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/sample4.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','phone_number','location']
print(a)
print('*'*100)
b=a.sort_values(by='age')
print(b)
print('*'*100)
c=a.sort_values(by='lname',ascending=False)
print(c)