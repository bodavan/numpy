# mathematics

import numpy as np
a = np.ones([2,3])
b = np.full([3,3],2)
print("a= \n",a,"\nb= \n",b)
#2D matrix multiplication >>  np.matmul(var1,var2)
# we need to 1st matrix column + 2nd matrix row
multiply = np.matmul(a,b)
print("a*b =\n",multiply)

# eliment wise multiply
a = np.array([i for i in range(10)]).reshape(2,5)
print("eliment wise multiply:\n",np.multiply(a,10))

# find the determinant

x = np.identity(3)
print("determinant\n",np.linalg.det(x))

# statistic
st =np.array([[1,2,3],[4,5,6]])
print("st:\n",st)

#minimum of all np.min(var)
print("min of all\n",np.min(st))

# min by row wise  np.min(var,axis=1)
print("min by row wise \n",np.min(st, axis=1))

# max by row wise  np.min(var,axis=1)
print("max by row wise \n",np.max(st, axis=1))

# sum    np.sum(var)
print("sum of all= \n",np.sum(st))

# sum by column wise   np.sum(var,axis=0)
print("sum by column wise=\n",np.sum(st,axis=0))

# sum by row wise   np.sum(var,axis=1)
print("sum by row wise=\n",np.sum(st,axis=1))