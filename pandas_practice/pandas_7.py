
import pandas as pd

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/heart.csv")
print(df.isna().sum())
print("*"*100)

x=df['trestbps'].mode()[0]
df.fillna(x,inplace=True)
print("*"*100)
df.dropna(subset='trestbps',inplace=True,ignore_index=True)
print(df)
print(df.isna().sum())
