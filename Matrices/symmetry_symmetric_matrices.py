import numpy as np

# sizes
m = 5
n = 5

# create matrices
A = np.random.randint(0,5,size=(m,n))
B = np.random.randint(0,5,size=(m,n))
AS = (A+A.T)/2
BS = (B+B.T)/2

print('AS: \n', AS), print(' ')
print('BS: \n', BS), print(' ')

print('sum: \n', AS + BS), print(' ')
print('product: \n', AS@BS), print(' ')
print('hadamard: \n', AS*BS), print(' ')

C_sum = AS + BS
C_prod = AS@BS
C_hada = AS*BS

# sum is santil symmetric
print('Symmetic?: \n', C_sum - C_sum.T), print(' ')
# product is not symmetric
print('Symmetic?: \n', C_prod - C_prod.T), print(' ')
# hadamard is santil symmetric 
print('Symmetic?: \n', C_hada - C_hada.T), print(' ')


# elementwise operations will maintain symmetry, non-element wise operations will not




