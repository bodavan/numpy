import numpy as np
main = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,56,67,89])
new = main.reshape(2,3,3)
# it is 3D array
# (2,3,3) means make 2 array and row 3 column 3
print(new)
# makeing array by tuple
a3 = np.array([((1,2,3,4),(6,7,8,9),(3,6,7,2)),((4,3,3,6),(4,5,6,2),(8,6,5,8))])
print("3d array by tuple\n",a3)
print("dimention: ",a3.ndim)
print("shape :",a3.shape)
# accessing eliment in 3D
# array number,row number ,column number
print("2nd array 1-r & 2-c : ",a3[1][1][2])
#changeing elemient
a3[0][2][2]=27
print(a3)

n3 = np.array([[[1,2,3],[3,4,5]],[[2,5,6],[3,4,5]]])
print("new 3d manually: \n",n3)
# accessing 3D eliment
print("accessing elemient : ",n3[0,1,2])
print('get first row : \n',n3[:,0,:])