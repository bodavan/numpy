import numpy as np
ar1 = np.array([[1,2,3],[4,5,6]])
print("main:\n",ar1)

print("its sqrt = \n",np.sqrt(ar1))
print("it's power 2 : \n",np.power(ar1,2))
print("its exponential : \n",np.exp(ar1))
print("its logarithm :\n",np.log(ar1))

# indexing matrix
a = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],
              [16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
print("the amtrix: \n",a)
print("the index of 11,12 & 16,17 is :- ",a[2:4,0:2])

print("the index of 2,8,14,20 will be : ",a[[0,1,2,3],[1,2,3,4]])