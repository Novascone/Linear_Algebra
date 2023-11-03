import numpy as np

A = np.reshape(np.arange(1,13),(3,4),'F') # F = column, C = row

r = [10, 20, 30, 40] # rows
c = [100, 200, 300] # columns

print('A: \n', A), print(' ')
print('r:', r), print(' ')
print('c:', c), print(' ')

# broadcast on the rows
print('A+r: \n', A+r), print(' ')
# broadcast on the columns
# reshape c into a column vector
print('c: \n', c), print(' ')
c = np.reshape(c, (len(c), 1))
print('c column: \n', c), print(' ')
print('A+c: \n', A+c), print(' ')
