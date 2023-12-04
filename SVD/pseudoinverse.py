import numpy as np
import inspect


A = np.array([[1,2,3],
              [1,2,4],
              [1,2,5]])

U,s,V = np.linalg.svd(A)

# pseudoinvert s

nonzeros = s>10**-14 # find nonzero elements
s[nonzeros] = 1/s[nonzeros] # invert the nonzero elements

# pseudoinvert A
Ai = V.T@np.diag(s)@U.T

print(Ai@A), print(' ')

print(np.linalg.pinv(A)@A),print(' ')

lines = inspect.getsource(np.linalg.pinv)
print(lines)