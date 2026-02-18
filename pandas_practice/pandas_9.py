
import pandas as pd

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/missing_data.csv")

#replace with mean where the Calories greater than 400


x=df['Calories'].mean()
print(x)
for i in df.index:
    if df.loc[i,'Calories']>400:
        df.loc[i,'Calories']=x
print(df)