import numpy as np
import matplotlib.pyplot as plt

## matrix powers

m = 4
n = 4

A = np.random.randint(0,6,size=(m,n))

# compute matrix power directly

A3 = np.linalg.matrix_power(A,3)
print(A3)
print(' ')

# via eigendecomposition

D,V = np.linalg.eig(A)
D = np.diag(D)

# via diagonalization

diagonal = V @ np.linalg.matrix_power(D,3) @ np.linalg.inv(V)

print(diagonal)
print(' ')

## eigenvalues of C and C^3

C = np.random.randint(0,6,size=(m,n))
C = C@C.T

Dc,Vc = np.linalg.eig(C)
D3,V3 = np.linalg.eig(C@C@C)

print(Vc),print(' ')
print(V3),print(' ')

plt.subplot(221)
plt.imshow(Vc)
plt.axis('off')
plt.title('evecs of C')

plt.subplot(223)
plt.imshow(V3)
plt.axis('off')
plt.title('evecs of C^3')

plt.show()

## plot eigenvectors and values 

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# plot eigenvectors C
ax.plot([0,Vc[0,0]],[0,Vc[1,0]],[0,Vc[2,0]],'b')
ax.plot([0,Vc[0,1]],[0,Vc[1,1]],[0,Vc[2,1]],'y')
ax.plot([0,Vc[0,2]],[0,Vc[1,2]],[0,Vc[2,2]],'r')

# plot eigenvectors of C^3
ax.plot([0,V3[0,0]],[0,V3[1,0]],[0,V3[2,0]],'b--')
ax.plot([0,V3[0,1]],[0,V3[1,1]],[0,V3[2,1]],'y--')
ax.plot([0,V3[0,2]],[0,V3[1,2]],[0,V3[2,2]],'r--')

plt.show()

# eigenvalues 

plt.plot([1,2,3,4],Dc,'bs-',label='C')
plt.plot([1.1,2.1,3.1,4.1],D3,'ys-',label='C^3')
plt.title('Eigenvalues')
plt.legend()
plt.show()

print(Dc), print(' ')
print(D3), print(' ')
print(Dc**3)