import numpy as np
import numpy.random as rn
import numpy.linalg as la
A=np.mat([[1,0,0],[0,1,0],[0,0,1]])
print('A=',A)

print(la.eig(A))