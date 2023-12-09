import numpy as np
import matplotlib.pyplot as plt


N = 1000
M = 20

# time vector
t = np.linspace(0,6*np.pi,N)

# relationship across channels 

chanrel = np.sin(np.linspace(0,2*np.pi,M))

data = np.zeros((M,N))

for i in range(M):
    data[i,:] = np.sin(t) * chanrel[i]
    
    # add noise
    
    data = data + np.random.randn(M,N)/10
    
    for i in range(M):
        data[i,:] = data[i,:] - np.mean(data[i,:])
        
cm = data@data.T/(N-1) 

fig,ax = plt.subplots(1,2,figsize=(12,5))

# draw timeseries
for i in range(M):
    ax[0].plot(t,data[i,:]+i*2)
ax[0].set_yticks([])
ax[0].set_ylabel('Channels')
ax[0].set_xlabel('Time (a.u.)')

ax[1].imshow(cm)
ax[1].set_ylabel('Channels')
ax[1].set_xlabel('Channels')

plt.show()

evals, evecs = np.linalg.eig(cm)

idx = np.argsort(evals)[::-1]
evals = np.real(evals[idx])
evecs = evecs[:,idx]

evals = 100*evals/np.sum(evals)

r = 2

comp_time_series = evecs[:,:r].T@data

fig = plt.subplots(121,figsize=(10,4))

plt.subplot(121)
plt.plot(evals,'s-')
plt.xlabel('Component number')
plt.ylabel('$\lambda$ (% total variance)')
plt.title('Eigenspectrum')

plt.subplot(122)
plt.plot(evecs[:,0],label='PC1')
plt.plot(evecs[:,1],label='PC2')
plt.xlabel('Channel')
plt.ylabel('PC weight')
plt.title('Eigenvectors')
plt.legend()
plt.show()

plt.plot(chanrel)
plt.xlabel('Channel')
plt.ylabel('Channel weight')
plt.title('Ground truth channel weights')
plt.show()

plt.plot(comp_time_series[0,:],label='PC1')
plt.plot(comp_time_series[1,:],label='PC2')
plt.xlabel('Time (a.u)')
plt.ylabel('Activity')
plt.title('Time course plots')
plt.legend()
plt.show()