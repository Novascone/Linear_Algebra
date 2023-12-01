import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

# compare eig(S,R) with eig(inv(R)@S)

S = np.random.randn(2,2)
R = np.random.randn(2,2)

Ls,Ws = scipy.linalg.eig(S,R)
Li,Wi = scipy.linalg.eig(np.linalg.inv(R)@S)

print(Ls)
print(Li)

# plot eigenvectors

plt.plot([0,Ws[0,0]],[0,Ws[1,0]], 'y')
plt.plot([0,Ws[0,1]],[0,Ws[1,1]], 'y--')
plt.plot([0,Wi[0,0]],[0,Wi[1,0]], 'b')
plt.plot([0,Wi[0,1]],[0,Wi[1,1]], 'b--')

plt.axis('square')
plt.grid()
plt.axis([-1,1,-1,1])
plt.show()
