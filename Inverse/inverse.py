import numpy as np 
import matplotlib.pyplot as plt

# size
m = 3

# random matrix
A = np.random.randn(m,m)

# compute inverse
Ainv = np.linalg.inv(A)

idm = A@Ainv

print(idm)

# show an image

plt.subplot(131)
plt.imshow(A)
plt.title('Matrix A')

plt.subplot(132)
plt.imshow(Ainv)
plt.title('Matrix $A^{-1}$')

plt.subplot(133)
plt.imshow(idm)
plt.title('AA$^{-1}$')

# pseudoinverse of a rectangular matrix

pseudoInvA = np.linalg.pinv(A)

plt.subplot(131)
plt.imshow(A), plt.axis('off')
plt.title('A')

plt.subplot(132)
plt.imshow(pseudoInvA), plt.axis('off')
plt.title('Pseudoinverse of A')

plt.subplot(133)
plt.imshow(pseudoInvA@A), plt.axis('off')
plt.title('A$^*$A')


# random matrix

n = 50 

A = np.random.randn(n,n)

A[:,n-1] = A[:,n-2]

# rank of A
print('rank =',np.linalg.matrix_rank(A))

Ai = np.linalg.pinv(A)

plt.subplot(221)
plt.imshow(A), plt.axis('off')
plt.title('A')

plt.subplot(222)
plt.imshow(Ai), plt.axis('off')
plt.title('A$^*$')

plt.subplot(223)
plt.imshow(Ai@A), plt.axis('off')
plt.title('A$^*$A')

plt.subplot(224)
plt.imshow(A@Ai), plt.axis('off')
plt.title('AA$^*$')

plt.show()