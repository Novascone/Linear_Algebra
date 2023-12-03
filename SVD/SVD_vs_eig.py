import numpy as np
import matplotlib.pyplot as plt

A = np.random.randint(1,6,size=(4,4))

A = A+A.T

print(A),print(' ')



L,W = np.linalg.eig(A)
U,S,V = np.linalg.svd(A)

# sort eig outputs to compare with SVD

sidx = np.argsort(L)[::-1]
L = L[sidx]
W = W[:,sidx]

fig,ax = plt.subplots(2,3,figsize=(10,7))
ax[0,0].imshow(W)
ax[0,0].set_title('W')
ax[0,1].imshow(np.diag(L))
ax[0,1].set_title('L')
ax[0,2].imshow(np.zeros((1,1)))

ax[1,0].imshow(U)
ax[1,0].set_title('U')
ax[1,1].imshow(np.diag(S))
ax[1,1].set_title('$\Sigma$')
ax[1,2].imshow(V)
ax[1,2].set_title('V$^T$')

plt.show()

print('V: \n', V),print(' ')
print('U: \n', U),print(' ')
print('W: \n', W),print(' ')

print('U - V: \n', np.round(U-V,4)),print(' ') 
print('U - W: \n', np.round(U- -W,4)),print(' ')
