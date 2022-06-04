# reorganizing arrays
import numpy as np
# we can reshaping our axisting array or matrix
x = np.array([[2,4,6,8],[1,3,5,7]])
print("its axisting array: \n",x)

y1 = x.reshape((8,1))
print("reshpeing 1 =\n",y1)

y2 = x.reshape([4,2])
print("its reshaping 2 = \n",y2)

y3 = x.reshape([2,2,2])
print("its reshaping 3 = \n",y3)



# vertically stacking
# np.vstack(var1,var2)
a = np.array([11,22,33,44,55])
b = np.array([9,7,5,8,2])
var1 = np.vstack([a,b])
print("stacking type 1 =\n",var1)

#we can stack as may time and anywere we want copying the arrays
var2 = np.vstack([b,a,b,b,a])
print("stacking type 2 =\n",var2)


#horizontal stack
h1 = np.array([44,90,56])
h2 = np.array([3,6,3,4])
print("horizontal stacking 1 =\n",np.hstack([h1,h2]))
# in matrix we need to take same row number for horzontal stacking
h3 = np.ones([2,4])
h4 = np.full([2,3],7)
print("horizontal stacking 2 =\n",np.hstack([h3,h4]))
