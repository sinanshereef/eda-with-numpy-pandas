

import numpy as np
import pandas as pd

a=pd.read_csv("C:/Users/zinan/OneDrive/Documents/movies_cleaned_pandas.csv",sep=',',header=None)
a.columns=['order','Movie_name','year','rate','box_office']
print(a)