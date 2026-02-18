

import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/sample4.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','phone_number','location']
df1=a[['fname','lname','age']].tail(2)  #last two emp of their fname,lname and age
print(df1)