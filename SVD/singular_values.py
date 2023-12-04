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

Ascaled = A*123

# svd

U,s,V = np.linalg.svd(Ascaled)

spct = 100*s/np.sum(s)

fig = plt.subplots(1,figsize=(7,5))

plt.subplot(211)
plt.plot(s,'ks-')
plt.xlabel('Component number')
plt.ylabel('$\sigma$')
plt.title('Raw singular values')

plt.subplot(212)
plt.plot(spct,'ks-')
plt.xlabel('Component number')
plt.ylabel('$\sigma$ (% of total)')
plt.title('Percent-change-normalized singular values')

plt.tight_layout()
plt.show()

