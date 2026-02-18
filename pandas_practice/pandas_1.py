
import pandas as pd

#DataFrame.....

lst=[1,100,30,2,78,2]
a=pd.DataFrame(lst)
print(a)
print(a.ndim)
print(a.dtypes)
print(a.describe())

#Series..........

lst=[1,100,30,2,78,2]
a=pd.Series(lst)
print(a)
print(a.ndim)
print(a.dtypes)