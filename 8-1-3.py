#數值積分-辛普森法
#x^2
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2

def simpson(a,b,n):
    if n%2==0:
        n=n
    else:
        print('非偶數區間，程式將區間+1')
        n=n+1

    h=(b-a)/n
    s1=0
    s2=0

    for i in range(1,n,2): #x1~xn-1,間隔2
        s1=s1+f(a+h*i)
    
    for i in range(2,n-1,2): #x2~xn-2,間隔2
        s2=s2+f(a+h*i)


    total=(h/3)*(f(a)+4*s1+2*s2+f(b))

    return(total)


    
    
    