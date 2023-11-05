import numpy as np
n = 4

N = np.random.randint(0,11,(n,n)) # non-symmetric
S = np.round(N.T*N / n**2) # symmetric

w = np.array([-1, 0, 1, 2])

# with symmetric

print(S@w)
print(S.T@w)
print(w@S)
print(w.T@S.T)
print(w.T@S), print(' ')

# with non-symmetric

print(N@w)
print(N.T@w)
print(w@N)
print(w.T@N.T)
print(w.T@N)

