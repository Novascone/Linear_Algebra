import numpy as np
import matplotlib.pyplot as plt

matrixSizes = np.arange(2,71)
cnums = np.linspace(10,1e12,40)

normdiffs = np.zeros((len(matrixSizes), len(cnums)))

for i,M in enumerate(matrixSizes):
    for j,C in enumerate(cnums):
        
        U = np.linalg.qr(np.random.randn(M,M))[0]
        V = np.linalg.qr(np.random.randn(M,M))[0]
        s = np.diag(np.linspace(C,1,M))
            
        A = U@s@V

        I = A@np.linalg.inv(A)
        diffeyes = I-np.eye(M)**2

        normdiffs[i,j] = np.linalg.norm(diffeyes)

fig = plt.figure(figsize=(7,7))
plt.pcolor(cnums,matrixSizes,normdiffs,vmax=np.max(normdiffs)*.6)
plt.xlabel('Condition Number')
plt.ylabel('Matrix size')
plt.colorbar()

plt.show()