import numpy as np
import matplotlib.pyplot as plt


# eigendecomposition of A

# symmetric matrix because symmetric matrices won't have complex eigenvalues
m = 4
n = 4
A = np.round(10*np.random.randint(1,6,size=(m,n)))
A = A.T@A

# eigendecomposition

evals,evecs = np.linalg.eig(A) 

# test reconstruction
Ap = evecs @ np.diag(evals) @ np.linalg.inv(evecs)

# plot
plt.subplot(121)
plt.imshow(A)
plt.axis('off')
plt.title('A')

plt.subplot(122)
plt.imshow(Ap)
plt.axis('off')
plt.title('$\lambda V^{-1}$')

plt.show()
recondiff = A-Ap

rmsA = np.sqrt( np.mean(np.square(np.reshape(recondiff,(1,-1)) )) )

print('Reconstruction RMS:', rmsA)

## diagonalization in images 

B = np.random.randint(1,101,size=(10,10))
B = B.T@B

# eigendecomposition
D,V = np.linalg.eig(B)

# show the results
plt.subplot(141)
plt.imshow(B)
plt.title('B')
plt.axis('off')

plt.subplot(142)
plt.imshow(V)
plt.title('V')
plt.axis('off')

plt.subplot(143)
plt.imshow(np.diag(D))
plt.title('$\Lambda$')
plt.axis('off')

plt.subplot(144)
plt.imshow(np.linalg.inv(V))
plt.title('$V^{-1}$')
plt.axis('off')

plt.show()