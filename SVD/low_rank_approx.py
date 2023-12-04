import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

m = 40
n = 30

# define a 2D Gaussian for smoothing
k = int( (m+n)/4)
xx = np.linspace(-3,3,k)
[X,Y] = np.meshgrid(xx,xx)
g2d = np.exp(-(X**2 + Y**2) / (k/8))

# matrix

A = sp.signal.convolve2d(np.random.randn(m,n),g2d,'same')



# svd V comes out as transposed

U,s,V = np.linalg.svd(A)

# number of layers to keep

nComps = 5

# reduced matrices
Ur = U[:,0:nComps]
sr = s[0:nComps]
Vr = V[0:nComps,:]

# low rank approximation
reconImage = Ur@np.diag(sr)@Vr

# rank

print('rank =',np.linalg.matrix_rank(reconImage))

# error map 

errormap = (reconImage-A)**2

plt.subplot(131)
plt.imshow(A)
plt.title('Original')
plt.axis('off')

plt.subplot(132)
plt.imshow(reconImage)
plt.title('Reconstruction')
plt.axis('off')

plt.subplot(131)
plt.imshow(A)
plt.title('Original')
plt.axis('off')

plt.subplot(133)
plt.imshow(errormap, vmin=-1,vmax=1)
plt.title('Error Map')
plt.axis('off')


plt.show()