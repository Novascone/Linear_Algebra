import numpy as np

# create two random integer vectors (R4)
n = 100
v = np.random.randint(n, size=4)
w = np.random.randint(n, size=4)
print(v)
print(w)
vl = np.sqrt(np.dot(v,v))
wl = np.sqrt(np.dot(w,w))
dpm = abs(np.dot(v,w))
# compute the lengths of the vectors, and the magnitude of the dot product 
print('length v:', vl)
print('length w:', wl)
print('dot mag:', abs(np.dot(v,w)))

# "normalize" the vectors 
muv = 1/vl
muw = 1/wl
unitv = v*muv
unitw = w*muw

print('unit v:', unitv)
print('unit w:', unitw)
# compute the magnitude of that dot product 
print('unit mag:', abs(np.dot(unitv,unitw)))