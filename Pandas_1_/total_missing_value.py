

import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/customer1.txt",sep=',',header=None)
a.columns=['id','fname','lname','age','prof','location']

#total no:of missing value
print(a.isna().sum())

#fill===> using fillna()
df=a.fillna('india')
print(df.isna().sum())
