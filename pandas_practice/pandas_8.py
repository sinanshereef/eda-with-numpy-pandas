
import pandas as pd

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/missing_data.csv")
x=df['Calories'].mode([0])
print(type(x))
df.loc[28,'Calories']=x.values[0]
print(df)