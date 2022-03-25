import numpy as np

def g(x):
    return(np.log(2*x+1))

i=1
x=1

tol=10**(-14)
while abs(x-g(x))>tol:
    print(i,x)
    i=i+1
    x=g(x)
    
     