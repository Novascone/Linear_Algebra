import numpy as np

M = np.random.randint(10,size=(3,3))

print(M), print(' ')
print(M.T), print(' ')
print(M.T.T), print(' ')

print(np.transpose(M))

# be careful with complex matricies

C = np.array([[4+1j, 3, 2-4j]])
print(C), print(' ')
print(C.T), print(' ')
print(np.transpose(C)), print(' ')

# in matlab the transpose is the Hermitian Transpose
# in python we have to call the Hermitian Transpose
# we do this by converting the array to a matrix and taking the Hermitian transpose
print(np.matrix(C).H)
# notice how the signs flip