import numpy as np
import matplotlib.pyplot as plt

A = [[1,2],[2,3]]

n = 30

wRange = np.linspace(-2,2,n)

qf = np.zeros((n,n))

for xi in range(n):
    for yi in range(n):
        w = np.transpose([wRange[xi], wRange[yi]])
        
        qf[xi,yi] = w.T@A@w / (w.T@w)
        
D,V = np.linalg.eig(A)

V = V*2

plt.imshow(qf,extent=[-2,2,-2,2])


plt.plot([0,V[0,0]], [0,V[1,0]])
plt.plot([0,V[0,1]], [0,V[1,1]])
plt.show()
