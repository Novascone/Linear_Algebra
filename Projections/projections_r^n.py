import numpy as np
import matplotlib.pyplot as plt

# sizes

m = 16
n = 10

# vector b

b = np.random.randint(m,size=m)

# matrix A

A = np.random.randint(1,10,size=(m,n))

x1 = np.linalg.inv(A.T@A) @ (A.T@b)

x2 = np.linalg.solve(A.T@A, A.T@b)

print(np.round(x1, 2))
print(np.round(x2, 2))

# geometric

m1 = 3
n1 = 2

b1 = np.random.randint(m1,size=m1)

A1 = np.random.randint(1,10,size=(m1,n1))

x = np.linalg.solve(A1.T@A1,A1.T@b1)
Ax = A1@x

print(b1.T)
print(Ax.T)

# plot 
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.add_subplot(projection='3d')

ax.plot([0, b1[0]], [0, b1[1]], [0, b1[2]], 'r')
ax.plot([0, Ax[0]], [0, Ax[1]], [0, Ax[2]], 'b')

ax.plot( [Ax[0], b1[0]],
         [Ax[1], b1[1]],
         [Ax[2], b1[2]], 'g')

xx, yy = np.meshgrid(np.linspace(-2,2), np.linspace(-2,2))
cp = np.cross(A1[:,0], A1[:,1])
z1 = (-cp[0]*xx - cp[1]*yy)*1./cp[2]
ax.plot_surface(xx,yy,z1,alpha=.4)

plt.show()