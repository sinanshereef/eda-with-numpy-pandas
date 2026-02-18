
import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/missing_data.csv",sep=',')
print(a)
print(a.shape)
print(a.dtypes)
print(a.isna().sum())
b=a.fillna(2020)
print(b.isna().sum())
print(b)