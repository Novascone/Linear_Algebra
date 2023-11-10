import numpy as np

m = 10
n = 4



A = np.random.randint(0,6,size=(m,n))
B = np.random.randint(0,6,size=(n,m))
C = A@B


def reduced_rank_mult(m,n,r):
    n = r
    A = np.random.randint(0,6,size=(m,r))
    B = np.random.randint(0,6,size=(r,n))
    C = A@B
    
    return C

    
    