

import numpy as np
import pandas as pd
a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/missing_data.csv",sep=',')
# print(a.dtypes)
# print(a.isna().sum())
# a.fillna(200,inplace=True)
# print(a)

# # calaries
# a['Calories'].fillna(310,inplace=True)
# #date
# a['Date'].fillna('2020/12/24',inplace=True)
# print(a)
# print(a['Calories'].unique())
# print('*'*100)
# x=a['Calories'].mean()
# print(x)
# a['Calories'].fillna(x,inplace=True)
# print(a)
# # a.dropna(inplace=True,ignore_index=True)
# # print(a)
# #calories missing data drop
# a.dropna(subset='Calories',inplace=True,ignore_index=True)
# print(a)
# x=a['Calories'].mean()
# a['Calories'].fillna(x,inplace=True)
# a.dropna(subset='Date',inplace=True,ignore_index=True)
# print(a)

#handle wrong data
# x=a['Duration'].mode()[0]
# a.loc[7,'Duration']=x
# print(a)
#calories==>400 wrong data assume
#mean()
# x=a['Calories'].mean()
# for i in a.index:
#     if a.loc[i,'Calories']>=400:
#         a.loc[i,'Calories']=x
# print(a)

#how to handle wrong format data
a['Date']=pd.to_datetime(a['Date'],format='mixed')
print(a)