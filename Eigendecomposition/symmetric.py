import numpy as np
import matplotlib.pyplot as plt

A = np.random.randn(14,14)

# symmetric
A = A+A.T

# diagonalize

evals,evecs = np.linalg.eig(A)

# magnitudes 
print(np.sqrt(sum(evecs**2))) # norm of each column


# plots

plt.imshow(A)
plt.axis('off')
plt.title('A')
plt.show()

plt.imshow(evecs)
plt.axis('off')
plt.title('Eigenvectors')
plt.show()

plt.imshow(evecs@evecs.T)
plt.axis('off')
plt.title('VV^T')
plt.show()


