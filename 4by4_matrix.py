

import numpy as np

a=np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2],[3,4,5,6]])
print(a)

print('*'*100)

print(a.reshape(1,2,8))

print('*'*100)

print(a.reshape(16,))