import numpy as np

A = np.random.randint(1,6,size=(4,4)) # square

U,s,V = np.linalg.svd(A)

normU = np.linalg.norm(U,2)
normV = np.linalg.norm(V.T,2)
normUV = np.linalg.norm(U@V,2)

print('norm U: \n', normU), print(' ')
print('norm V: \n', normV), print(' ')
print('norm U@V: \n', normUV), print(' ')

UUt = U@U.T
VtV = V.T@V
UV = U@V

print('U@Ut: \n', UUt), print(' ')
print('Vt@V: \n', VtV), print(' ')
print('U@V: \n', UV), print(' ')

C = U@V

print('C@Ct: \n', C@C.T), print(' ')


