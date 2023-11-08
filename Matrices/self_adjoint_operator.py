import numpy as np

# <Av, w> = <v, Aw> 
# condition 1
# if A is square
# condition 2
# if A is symmetric
# condition 3
# if v and w are the same size 

# A has to be symmetic to so the the transpose of A equals A 

A = np.random.randint(0,5,size=(4,4))
v = np.random.randint(0,5,size=(4))
w = np.random.randint(0,5,size=(4))
A = A@A.T/2

print('dot(Av, w):\n', np.dot(A@v, w)), print(' ')
print('dot(Aw, v):\n', np.dot(A@w, v)), print(' ')


# print('Av.T:\n', np.transpose(A*v)), print(' ')
# print('Av.T:\n', np.transpose(A*v)), print(' ')


