
import pandas as pd
df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/missing_data.csv")
#wrong Format

df['Date']=pd.to_datetime(df['Date'],format='mixed')
print(df)