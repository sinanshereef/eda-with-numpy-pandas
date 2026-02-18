
import pandas as pd
df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/txn_windows.csv")
print(df)
#txn_windows
print('*'*100)
print(df.columns)
#1.Find Row count
print(df.shape[0])
#2.jan month oid,cusno,category,product,state
#A. Row count
dfjan = df.loc[df['dat'].str.startswith('01-')] [['oid', 'cuid', 'category', 'product', 'state']]
print(dfjan.shape[0])
print('*'*100)
#3.July Month oid,cusno,category,product,state
#B. Row count
dfjuly=df.loc[df['dat'].str.startswith('07-')] [['oid', 'cuid', 'category', 'product', 'state']]
print(dfjuly.shape[0])
print('*'*100)
#4.Each category [count desc sort]
df1=df.groupby('category')['category'].count().sort_values(ascending=False)
print(df1)
print('*'*100)
#5.Category full dea ls
df2 = df.loc[df['category'] == 'Outdoor Recrea on']
print(df2)
print('*'*100)
#6. Each paymethod count
df3=df.groupby('method')['method'].count().sort_values(ascending=False)
print(df3)
print('*'*100)
#7. jan-july month purchase count [include]
df4 = df.loc[
(df['dat'].str.startswith('01-')) |
(df['dat'].str.startswith('02-')) |
(df['dat'].str.startswith('03-')) |
(df['dat'].str.startswith('04-')) |
(df['dat'].str.startswith('05-')) |
(df['dat'].str.startswith('06-')) |
(df['dat'].str.startswith('07-'))
]
print(df4.shape[0])
print('*'*100)
#8.Each category total amount
df5=df.groupby('category')['pay_amount'].sum()
print(df5)
print('*'*100)
#9.Each category maximum amount
df6=df.groupby('category')['pay_amount'].max()
print(df6)
print('*'*100)
#10.Each category avg amount
df7=df.groupby('category')['pay_amount'].mean()
print(df7)
print('*'*100)
#11.total amount by cash and credit card
df8=df.groupby('method')['pay_amount'].sum()
print(df8)
print('*'*100)
#12.Indoor games ,total amount
df9=df.loc[df['category']=='Indoor Games'] ['pay_amount'].sum()
print(df9)
print('*'*100)
#13.Each state count
df10=df.groupby('state')['state'].count()
print(df10)
print('*'*100)