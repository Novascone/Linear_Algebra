import numpy as np
import matplotlib.pyplot as plt

m = 40
n = 40

for i in range(0,200):
    A = np.random.randint(1,6,size=(m,n))
    eigenA = np.linalg.eig(A)[0]
    plt.plot(np.real(eigenA),np.imag(eigenA), 's', markersize=1)
    
plt.axis('square')
plt.show()
