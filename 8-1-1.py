#數值積分-中點法
#求f(x)在[a,b]區間的定積分

import numpy as np

def midpoint_int(a,b,n):
    x=np.linspace(a,b,n+1) #在[a,b]中包含a.b共有n+1個數(即分成n段) 
    #h=(b-a)/n
    sum=0

    for i in range(n):  #i在0~n-1的區間內
        xmi=(x[i]+x[i+1])/2
        sum=sum+(x[i+1]-x[i])*f(xmi)
    
    return(sum)

def f(x):
    return x**2

a=0
b=1

print(midpoint_int(a,b,100))
        

