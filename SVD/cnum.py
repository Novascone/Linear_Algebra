import numpy as np

m = 6
n = 16
cnum = 41.99

U,junk = np.linalg.qr(np.random.randn(m,m))
V,junk = np.linalg.qr(np.random.randn(n,n))

s = np.linspace(cnum,1,np.min([m,n]))
S = np.zeros((m,n))
for i in range(len(s)):
    S[i,i] = s[i]
    
A = U@S@V.T
cnum = np.linalg.cond(A)
print(cnum)