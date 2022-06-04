import numpy as np
larg = np.array([i for i in range(25)])
larg = larg.reshape(5,5)
print(larg)

# dot prodact
ar1 = np.array([[2,3],[5,6]])
ar2 = np.array([[2,8],[7,3]])
print(ar1 @ ar2)
print(ar1.dot(ar2))
print(np.dot(ar2,ar1))