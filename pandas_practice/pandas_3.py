import pandas as pd

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/custom_windows.csv")
a=df.drop(['salary'],axis=1)
print(a)