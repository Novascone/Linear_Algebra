import numpy as np
import matplotlib.pyplot as plt

A = [ [1,0],
      [1,0],
      [0,1] ]

# "full" QR decomposition
Q,R = np.linalg.qr(A, 'complete')
print(Q), print(' ')

# "economy" QR decomposition
Q,R = np.linalg.qr(A)
print(Q)

## another example

# to-be-decomposed

M = np.array([[1, 1, -2], [3, -1, 1] ])

# QR decomposition

Q,R = np.linalg.qr(M, 'complete')

print('R from QR: '), print(np.round(R,4))
print('R from Q^TA: '), print(np.round(Q.T@M,4))

# plot 

colorz = 'krg'

for i in range(0, np.shape(M)[1]):
    
    # plot original vector Q
    plt.plot([0,M[0,i]],[0,M[1,i]],colorz[i])
    
    # plot orthogonalized Q
    if i<np.shape(Q)[1]:
        plt.plot([0,Q[0,i]], [0,Q[1,i]],colorz[i],linestyle='--')
        
    # plot residual vector R
    plt.plot([0,R[0,i]],[0,R[1,i]],colorz[i],linestyle=':')
    
plt.legend(['M$_1$', 'Q$_1$', 'R$_1$'])
plt.axis('square')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.grid(True)
plt.plot()

plt.show()