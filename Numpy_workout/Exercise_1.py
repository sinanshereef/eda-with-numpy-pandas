

import numpy as np

#1.Create a NumPy array of shape (5,5) with random integers between 1 and 100.

a=np.random.randint(1,101,size=(5,5))
print(a)

# 2.Given a NumPy array, find the mean, median, and standard deviation.

b=np.array([2,34,5,7,32,2,2,3,344,54,3,1])
print(b.mean())
print(np.median(b))
print(b.std())

# 3. Create a NumPy array and reshape it into a 3x4 matrix

print(b.reshape(3,4))

# 4. Generate a NumPy array of 50 numbers evenly spaced between 0 and 10.

v=np.linspace(0,11,50)
print(v)

# 5. Given a 2D NumPy array, extract all elements greater than the average value of the array.

s=np.array([[20 ,384,1,24,455,22,4566,212,123,455,700,2,200,98673]])
avg=s.mean()
lst=[]
for i in s.flatten():
    if i>avg:
        lst.append(i)
print(lst)