import numpy as np
from reduced_rank_mult import reduced_rank_mult

m = 6
n = 4

A = np.random.randint(0,6,size=(m,n))
b = np.random.randint(0,6,size=(m,n))
B = reduced_rank_mult(m,n,3)
l = np.random.randint(1,4)

Rank_A = np.linalg.matrix_rank(A)
Rank_B = np.linalg.matrix_rank(B)
Rank_Al = np.linalg.matrix_rank(l*A)
Rank_Bl = np.linalg.matrix_rank(l*B)
l_rank = l*np.linalg.matrix_rank(A)



print('Rank A:\n', Rank_A), print(' ')
print('Rank B:\n', Rank_B), print(' ')
print('Rank Al:\n', Rank_Al), print(' ')
print('Rank Bl:\n', Rank_Bl), print(' ')

