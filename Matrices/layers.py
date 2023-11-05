import numpy as np

# A = np.random.randint(0,3,size=(2,2))
# B = np.random.randint(0,3,size=(2,2))
A = np.array([[0, 1], [2, 3]])
B = np.array([[2, 2], [1, 0]])
# C = np.zeros((2,2))
C = []
for i in range(len(A)):
    C.append(np.outer(A[:,i], B[i,:]))
    
C = C[0] + C[1]
np.asarray(C)
print('Layer:\n',C)
print('numpy:\n',np.matmul(A,B))


# print(C[1])