
import pandas as pd

# 1. Load the dataset using pandas and display the first 3 rows

df=pd.read_csv("C:/Users/zinan/OneDrive/Documents/practice_pandas_dataset.csv")
print(df.head(3))
print("*"*100)
print(df)

# 2. Check for missing values in each column
print("*"*100)
print(df.isna().sum())

# 3. Find the average age of all individuals
print("*"*100)
print(df['age'].mean())

# 4. Filter rows where salary is greater than 50,000
print("*"*100)
a=df.loc[df['salary']>50000]
print(a)

# 5. Sort the data by age in descending order.
print("*"*100)
b=df.sort_values(by='age',ascending=False)
print(b)

# 6. Group the dataset by “department” and find the average salary
c=df.groupby(by='department') ['salary'].mean()
print(c)

# 7. Add a new column “tax” = salary * 0.1

df['tax']=df["salary"] * 0.1
print(df)

# 8. Save the modified DataFrame into a new CSV file

df.to_csv("C:/Users/zinan/OneDrive/Documents/Updated_or_completed.csv",index=True)