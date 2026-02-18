

import pandas as pd

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/heart.csv")

a=df.groupby('age') ['age'].sum()
print(a)