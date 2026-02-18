
import numpy as np
import pandas as pd
a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/student.csv",sep=',')
b=pd.read_csv("C:/Users/zinan/OneDrive/Documents/result.csv",sep=',')
c=pd.merge(a,b,on='roll',how='inner')
d=c.loc[c['res']=='pass']
print(d)