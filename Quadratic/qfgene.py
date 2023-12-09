import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as linalg


m = 14
n = 1000

A = np.zeros((m,n))
for i in range(n):
    A[:,i] = np.random.randn(m) * np.cos(np.linspace(0,np.pi,m))
    
A = A@A.T


B = np.zeros((m,n))
for i in range(n):
    B[:,i] = np.random.randn(m) * np.cos(np.linspace(0,np.pi,m))
    
B = B@B.T

evals,evecs = linalg.eigh(A,B)


plt.subplots(231)
plt.imshow(evecs.T@evecs,extent=[-m,m,-m,m])
plt.xticks([])
plt.title('W$^T$W')

tmp = evecs.T@evecs
plt.subplots(234)
plt.plot(tmp[1,:],'s-')
plt.title('W$_j^T$W')

plt.subplots(232)
plt.imshow(evecs.T@A@evecs,extent=[-m,m,-m,m])
plt.xticks([])
plt.title('W$^T$AW')

plt.subplots(235)
plt.plot(np.diag(evecs.T@A@evecs),'s-')
plt.plot(evals,'r')
plt.title('diag(W$^T$AW)')

plt.subplots(236)
plt.plot(np.diag(evecs.T@B@evecs),'s-')
plt.title('diag(W$^T$BW)')

plt.show()
