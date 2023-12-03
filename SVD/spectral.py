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

# show matrices

fig = plt.subplots(1,figsize=(10,6))

plt.subplot(241)
plt.imshow(A)
plt.title('A')

plt.subplot(242)
plt.imshow(U)
plt.title('U')

plt.subplot(243)
plt.imshow(np.diag(s))
plt.title('$\Sigma$')

plt.subplot(244)
plt.imshow(V)
plt.title('V$^T$')

plt.subplot(212)
plt.plot(s,'ks-')
plt.xlabel('Component Number')
plt.ylabel('$\sigma$')
plt.title('Scree plot of singular values')

plt.show()

rank_one_maxtrices = np.zeros((5,m,n))

for i in range(0,5):
    
    rank_one_maxtrices[i,:,:] = np.outer(U[:,i]*s[i],V[i,:])
    
    plt.subplot2grid((2,5),(0,i))
    plt.imshow(rank_one_maxtrices[i,:,:],vmin=-5,vmax=5)
    plt.axis('off')
    plt.title('C.%d' %(i+1))
    
    plt.subplot2grid((2,5),(1,i))
    imdat = np.sum(rank_one_maxtrices[:i+1,:,:],axis=0)
    plt.imshow(imdat,vmin=-5,vmax=5)
    plt.axis('off')
    plt.title('C.%d' %(i+1))
    
plt.imshow(A)

plt.show()

    
