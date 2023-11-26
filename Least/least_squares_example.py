import numpy as np
import matplotlib.pyplot as plt

# data

data = np.array([[-4,0,-3,1,2,8,5,8]]).T
N = len(data)

# design matrix
# A = np.ones([N,1])
# fit the model
# x = np.linalg.solve(A.T@A,A.T@data)

# compare against mean
# m = np.mean(data)

# print(x, m)

# compute the model-predicted values

# plot data and model prediction
# bHat = A@x

# plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
# plt.plot(np.arange(1,N+1), bHat, 'ro--', label='Model pred.')

# plt.legend()
# plt.show()

# new design matrix
# A = np.array([np.arange(0,N)]).T

# fit model
# x = np.linalg.solve(A.T@A,A.T@data)

# compute the model predicted values
# bHat = A@x

# plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
# plt.plot(np.arange(1,N+1), bHat, 'ro--', label='Model pred.')

# plt.legend()
# plt.show()

# design matrix

# A = np.concatenate([np.ones([N,1]),np.array([np.arange(0,N)]).T], axis=1)

# fit model
# x = np.linalg.solve(A.T@A,A.T@data)

# compute the model predicted values
# bHat = A@x


# plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
# plt.plot(np.arange(1,N+1), bHat, 'ro--', label='Model pred.')

# plt.legend()
# plt.show()

# now with non linearity 

A = np.concatenate([np.ones([N,1]),np.array([np.arange(0,N)**2]).T], axis=1)

# fit model
x = np.linalg.solve(A.T@A,A.T@data)

# compute the model predicted values
bHat = A@x


plt.plot(np.arange(1,N+1),data,'bs-',label='Data')
plt.plot(np.arange(1,N+1), bHat, 'ro--', label='Model pred.')

plt.legend()
plt.show()

