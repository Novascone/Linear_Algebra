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
    
    data = data + np.random.randn(M,N)/3
    
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
