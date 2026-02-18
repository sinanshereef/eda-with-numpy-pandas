

import numpy as np
import pandas as pd
a=pd.DataFrame([[101,'Sinan','Shereef',23],
                [102,'Deepak','Prakash',21],
                [230,'jo','p',40],
                [370,'mike','k',34]])
a.columns=['id','fname','lname','age']
b=pd.DataFrame([['Engineer',230,'EKM',200],
                ['bigdata',101,'TVM',400],
                ['testing',102,'klm',234],
                ['python',370,'ktym',324]])
b.columns=['prof','id','location','salary']
c=pd.merge(a,b,on='id',how='outer')
print(c)