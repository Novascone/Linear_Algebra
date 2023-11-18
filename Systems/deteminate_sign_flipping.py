import numpy as np

m = 5
F = np.random.randint(1,10,size=(m,m))

for i in range(m-1):
    temp = np.array
    print('F:\n',F)
    print(np.linalg.det(F))
    temp = np.array(F[i,:])
    F[i,:] = F[i+1,:]
    F[i+1,:] = temp
    print('F:\n',F)
  
