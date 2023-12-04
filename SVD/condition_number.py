import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

m = 40
n = 40

# define a 2D Gaussian for smoothing
k = int( (m+n)/4)
xx = np.linspace(-3,3,k)
[X,Y] = np.meshgrid(xx,xx)
g2d = np.exp(-(X**2 + Y**2) / (k/8))

# matrix

A = np.random.randn(m,n)
# A = sp.signal.convolve2d(np.random.randn(m,n),g2d,'same')

s = np.linalg.svd(A)[1]

cnum = s[0]/s[-1]

plt.subplot(211)
plt.imshow(A)
plt.title('C num: %d' %cnum)
plt.axis('off')

plt.subplot(212)
plt.plot(s,'ks-')
plt.xlabel('C num')
plt.xlabel('$\sigma$')
plt.title('Singular Values')

plt.show()