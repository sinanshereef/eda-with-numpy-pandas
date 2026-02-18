
import numpy as np

sf=np.array([3,4,2,5,7,8,90,8,7,67,11,412,56])
#where
d=np.where(sf>10)
print(d)

#concept ==> Filter
b=sf>10
c=sf[b]
print(c)

