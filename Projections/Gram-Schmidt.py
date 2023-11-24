import numpy as np 

def GS(m,n):
    
    A = np.random.randint(0,5,size=(m,n))
    print(A)
    orth_cols = np.zeros(shape=(m,n))

    for i in range(len(A)):
        orth_cols[:,i] = A[:,i]
        a = A[:,i]
        
        for j in range(i):
            q = orth_cols[:,j]
            beta = np.dot(a,q)/np.dot(q,q)
            i_para = beta*q
            orth_cols[:,i] = orth_cols[:,i] - i_para
        orth_cols[:,i] =  orth_cols[:,i] / np.linalg.norm(orth_cols[:,i])
    return orth_cols

orth = GS(4,4)
print(np.round(orth.T@orth,3))

