import numpy as np
first = np.array([[1,2,3],[4,5,6]])
print('first matrix\n',first)
second = np.array([[2,4,6],[3,5,7]])
print("seccond matrix\n",second)

print('sum of two matrix:\n ',first + second)
print('multiple of two matrix : \n',first * second)

# dimension of matrix by . ndim
print("number of dimension of first matrix = ",first.ndim)

# number of row and column by .shape
print('second matrix shape means number of row and column: ',second.shape)

third_matrix = np.array([[23,45,56,78],[98,76,54,43],[80,79,57,35]])

print("third matrix \n",third_matrix)
# as the index start from 0
print('frome third matrix 2nd row 3rd column elimen : ',third_matrix[2,3])
print('frome third matrix 1st row 1st column elimen : ',third_matrix[1,-3])
#get specific row
print('just first row from third matrix: ',third_matrix[1,:])
print('just 3rd column from third matrix: ',third_matrix[:,2])

# changeing element
third_matrix[1,2] = 100
print("chenged1 third matrix : \n",third_matrix)
#changeing enter column
third_matrix[:,1] = [11,22,33]
print("chenged 1st column : \n",third_matrix)
#chenged 0th row
third_matrix[0,:] = [10,20,30,40]
print("chenged index o row : \n",third_matrix)
print("third matrix  = \n",third_matrix)

print("third matrix dimension = ",third_matrix.ndim)
print("third matrix row and column = ",third_matrix.shape)

# git size (means number of total eliment
print("third matrix size: ",third_matrix.nbytes)