import numpy as np
import matplotlib.pyplot as plt

S = np.zeros((4,), dtype=np.object_)

S[0] = [[4,  4],[4,  9]]
S[1] = [[4, -1],[3, -5]]
S[2] = [[0,  1],[2,  0]]
S[3] = [[1,  1],[1,  1]]

# range for vector w

n = 30
wRange = np.linspace(-2,2,n)

qf = np.zeros((n,n))
qfn = np.zeros((n,n))

for i in range(4):
    
    for xi in range(n):
        for yi in range(n):
            w = np.transpose([wRange[xi], wRange[yi]])
            
            qf[xi,yi] = w.T@S[i]@w
            
    plt.subplot(2,2,i+1)
    plt.imshow(qf,extent=[wRange[0],wRange[-1],wRange[0],wRange[-1]])

    
    
plt.show()

# 3D plotting

cmap_ = plt.get_cmap('gist_earth')

for i in range(4):
    
    for xi in range(n):
        for yi in range(n):
            w = np.transpose([wRange[xi], wRange[yi]])
            qf[xi,yi] = w.T@S[i]@w
            qfn[xi,yi] = (w.T@S[i]@w)/(w.T@w)
            
    X,Y = np.meshgrid(wRange,wRange)
    Z = qf.T
    Zn = qfn.T
    
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(221+i, projection='3d')
    surf = ax.plot_surface(X,Y,Z,cmap=cmap_)
    ax.view_init(azim=-30,elev=30)
    ax.set_title('Quadratic Form')
    
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(221+i, projection='3d')
    surf = ax.plot_surface(X,Y,Zn,cmap=cmap_)
    ax.view_init(azim=-30,elev=30)
    ax.set_title('Normalized Quadratic Form')
    
plt.show()    

