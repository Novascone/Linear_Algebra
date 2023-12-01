import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

A = np.array([[3,2], [1,3]])
B = np.array([[1,1], [4,1]])

# GED
evals,evecs = scipy.linalg.eig(A,B)

# matrix-vector multiplication

Av = A@evecs[:,1]
Bv = B@evecs[:,1]
BinvAv = np.linalg.inv(B)@A@evecs[:,1]

plt.plot([0, evecs[0,1]],[0,evecs[1,1]],'b',linewidth=4,label='$v_2$')
plt.plot([0, Av[0]],[0,Av[1]],'y--',linewidth=2,label='$Av_2$')
plt.xlim([-3,3]), plt.ylim([-3,3])
plt.plot([-3,3],[0,0],'y:')
plt.plot([0,0],[-3,3],'y:')
plt.legend()
plt.title('Av')
plt.show()


plt.plot([0, evecs[0,1]],[0,evecs[1,1]],'b',linewidth=4,label='$v_2$')
plt.plot([0, BinvAv[0]],[0,BinvAv[1]],'y--',linewidth=2,label='B$^{-1}$Av')
plt.xlim([-3,3]), plt.ylim([-3,3])
plt.plot([-3,3],[0,0],'y:')
plt.plot([0,0],[-3,3],'y:')
plt.legend()
plt.title('B$^{-1}$Av')
plt.show()