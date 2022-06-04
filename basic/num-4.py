# initialze different type of array

import numpy as np
# zero matrix
arr1 = np.zeros([2,3,4])
print("its zero matrix(3D): \n",arr1)

# all 1s matrix
arr2 = np.ones([3,4])
print("its ones matrix: \n",arr2)

# any other matrix (full)
# full((shape),number)
arr3 = np.full((3,4),67)
print("its by full : \n",arr3)
#full_like ((variable.shape),number)
x = [[34,56,78],[12,98,76]]
arr4 = np.full_like(x,3)
print("its by full_like: \n",arr4)

#random intiger value by random.ran(highst value or lowest to higest,size(row,colum))
arr5 = np.random.randint(130,size=(4,5))
print("itts random: \n",arr5)

# identity matrix (means = row number equal column number)
arr5 = np.identity(3)
print(arr5)

#repeat matrix

arr6 = np.array([[1,2,3,4]])
r1= np.repeat(arr6,3,axis=0)
print("repeat: \n",r1)

###
output = np.ones((5,5))
zero = np.zeros((3,3))
zero[1,1] = 9
output[1:-1,1:4] = zero
print("new complex:\n",output)

