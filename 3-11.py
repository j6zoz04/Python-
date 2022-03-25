#割線法
#求解f(x)=e^x-2x-1的根 (已知一個根為0)
#並比較牛頓法和切線法的收斂速度
import numpy as np

def f(x):
    return np.exp(x)-2*x-1
def df(x):
    return np.exp(x)-2

#牛頓法需要一個起始值
def Newton_Method(x0):
    i=0
    tol=10**(-16)
    while abs(f(x0))>tol:
        x1=x0-f(x0)/df(x0)
        i=i+1
        x0=x1

    return(i,x1,f(x0))

#割線法需要兩個起始值
def Secant_Method(x0,x1):
    i=0
    tol=10**(-16)
    while abs(f(x1))>tol:
        x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
        i=i+1
        x0=x1
        x1=x2
    return(i,x1,f(x1))

print(Newton_Method(100))
#print(Secant_Method())
