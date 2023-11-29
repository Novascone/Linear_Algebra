import numpy as np
import matplotlib.pyplot as plt

A = [[1,2],[2,1]]

# eigenvalues and eigenvectors
evals,evecs = np.linalg.eig(A)
print(evals), print(' ')
print(evecs) # normalize to unit length one

# magnitude of each eigenvector

mag1 = np.sqrt(np.sum(np.square(evecs[:,0])))
mag2 = np.sqrt(np.sum(np.square(evecs[:,1])))
print(mag1,mag2)

plt.plot([0,evecs[0,0]],[0,evecs[1,0]], 'y', label='v1')
plt.plot([0,evecs[0,1]],[0,evecs[1,1]], 'b', label='v2')
plt.axis([-5,5,-5,5])
plt.legend()
plt.show()