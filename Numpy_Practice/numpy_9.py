
#iteration...........

import numpy as np
a=np.array([[[1,2,3,4,5],[2,4,6,8,0],[1,3,5,7,9]]])

for i in a:
    for j in i:
        for k in j:
            print(k)