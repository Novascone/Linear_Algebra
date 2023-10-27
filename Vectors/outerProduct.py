import numpy as np

v = np.array([  1, 2, 3 ])
w = np.array([ -1, 0, 1 ])

np.outer(v,w)

op = np.zeros((len(v),len(w)))
for i in range(0,len(v)):
    for j in range(0, len(w)):
        op[i][j] = v[i] * w[j]
        
print(op)