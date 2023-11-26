import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

# load data
data = sio.loadmat('EEG_RT_data.mat')
rts = data['rts']
rts = rts[0]
EEGdata = data['EEGdata']
frex = data['frex']
frex = frex[0]

nTrials = len(rts)
nFrex = len(frex)

# show data 

# plt.plot(rts, 'ks-')
# plt.xlabel('Trial')
# plt.show()

# plt.imshow(EEGdata, origin='lower')
# plt.xlabel('Trial'), plt.ylabel('Frequency')
# plt.show()

A = np.concatenate([np.ones([nTrials-1,1]),                   # intercept
                    np.reshape(rts[0:-1], (nTrials-1,1)),     # RTs
                    np.reshape(EEGdata[10,:-1],(nTrials-1,1)) # brain
                    ],axis=1)

x1 = np.linalg.solve(A.T@A,A.T@rts[1:])
x2 = np.linalg.lstsq(A,rts[1:],rcond=None)[0]


# print(A)

# print(x1)
# print(x2)

# initialize coefficients vector

x = np.zeros(len(frex))

# loop over frequencies
for fi in range(0,len(frex)):
    
    # design matrix
    A = np.concatenate( [np.ones([nTrials,1]),
                         np.reshape(EEGdata[fi,:], (nTrials,1))
                         ], axis=1)
    # compute parameters 
    t = np.linalg.lstsq(A,rts,rcond=None)[0]
    x[fi] = t[1]
    
# plots 
plt.figure(figsize=(8,8))
plt.subplot(211)
plt.plot(frex,x,'rs-')
plt.xlabel('Frequency (Hz)')
plt.ylabel('coefficient')

plt.subplot(223)
plt.plot(EEGdata[8,:],rts,'ks')

plt.subplot(224)
plt.plot(EEGdata[23,:],rts,'ks')
plt.show()