
import  pandas as pd

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/heart.csv")
print(df.drop_duplicates())
print(df.isna().sum())
print(df.fillna(7,inplace=True))
print('*'*100)
print(df.isna().sum())
print(df[['age','sex','target']])
print("*"*100)

#iloc

df1=df.iloc[:5,:]
print(df1)
print('*'*100)
#loc

df2=df.loc[df['age']>23].sort_values(by='sex') [['age','target','chol','cp']].head(5)
print(df2)
