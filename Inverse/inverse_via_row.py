import numpy as np
from sympy import *
import matplotlib.pyplot as plt

# size 

m = 4

# random matrix
A = Matrix( np.round(10*np.random.randn(m,m)), dtype='float')

# augment A and Identity

Aaug = Matrix( np.concatenate((A,np.eye(m,m)), axis=1))
print('Size of Aaug:', Aaug.shape)

# rref
Asol = Aaug.rref()
Asol = Asol[0]
Ainvrref = Asol[:,m:m*2]
Ainv = A.inv()

# show the matrices
plt.subplot(211)
plt.imshow(matrix2numpy(Aaug, dtype='float'),vmin=-5,vmax=5)
plt.title('A|I'), plt.axis('off')

plt.subplot(212)
plt.imshow(matrix2numpy(Asol,dtype='float'))
plt.title('I|A$^{-1}$'), plt.axis('off')

# show square matrices
plt.subplot(131)
plt.imshow(matrix2numpy(A,dtype='float'))
plt.title('Matrix A'), plt.axis('off')

plt.subplot(132)
plt.imshow(matrix2numpy(Ainvrref,dtype='float'))
plt.title('Matrix A'), plt.axis('off')

plt.subplot(133)
plt.imshow(matrix2numpy(Ainv,dtype='float'))
plt.title('Matrix A'), plt.axis('off')


plt.show()