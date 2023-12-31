import numpy as np
import matplotlib.pyplot as plt

S = np.zeros((5,), dtype=np.object_)
S[0] = [ [ 4,   4], [ 4,  9] ]
S[1] = [ [-4,  -1], [-3, -5] ]
S[2] = [ [ 0,  -1], [ 2,  0] ]
S[3] = [ [ 1,   1], [ 1,  1] ]
S[4] = [ [-1,  -2], [-3, -6] ]

n = 30
wr = 2
wRange = np.linspace(-wr,wr,n)

qf = np.zeros((n,n))

fig = plt.subplots(1,figsize=(8,8))

for i in range(5):
    
    for xi in range(n):
        for yi in range(n):
            w = np.transpose([wRange[xi], wRange[yi]])
            
            qf[xi,yi] = w.T@S[i]@w
            
    plt.subplot(2,3,i+1)
    plt.imshow(qf.T,extent=[-wr,wr,-wr,wr])
    
    
    evals = np.linalg.eig(S[i])[0]

    esign = np.sign(evals)

    if sum(esign)==2:
        defcat = 'Pos. def.'
    elif sum(esign)==1:
        defcat = 'Pos. def.'
    elif sum(esign)==0:
        defcat = 'Indeterminant'
    elif sum(esign)==-1:
        defcat = 'Neg. semidef.'
    elif sum(esign)==-2:
        defcat = 'Neg. def.'
    
    plt.title(defcat)


plt.show()