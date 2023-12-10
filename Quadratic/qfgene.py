import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as linalg


m = 14
n = 1000

A = np.zeros((m,n))
for i in range(n):
    A[:,i] = np.random.randn(m) * np.cos(np.linspace(0,np.pi,m))
    
A = A@A.T


B = np.zeros((m,n))
for i in range(n):
    B[:,i] = np.random.randn(m) * np.cos(np.linspace(0,np.pi,m))
    
B = B@B.T

evals,evecs = linalg.eigh(A,B)


