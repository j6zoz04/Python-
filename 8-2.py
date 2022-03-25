#中點法的誤差
#梯形法的誤差
#辛普森法的誤差
import numpy as np
import matplotlib.pyplot as plt
#中點法:
def midpoint_int(a,b,n):
    x=np.linspace(a,b,n+1) #在[a,b]中包含a.b共有n+1個數(即分成n段) 
    #h=(b-a)/n
    sum=0

    for k in range(n):  #i在0~n-1的區間內
        xmk=(x[k]+x[k+1])/2
        sum=sum+(x[k+1]-x[k])*f(xmk)
    
    return(sum)
#梯形法:
def trap(a,b,n):
    x=np.linspace(a,b,n+1) #x會是一個陣列(array)
    x=np.delete(x,[0,n])
    h=(b-a)/n
    fk=f(x) #列表(list)無法對裡面的元素做數學運算，但陣列(array)可以
    s=h*(0.5*(f(a)+f(b))+sum(fk)) #利用sum函數即可不用for迴圈

    return(s)
#辛普森法
def simpson(a,b,n):

    if n%2==0:
        n=n
    else:
        n=n+1

    x=np.linspace(a,b,n+1)
    h=(b-a)/n

    s1=0
    s2=0
    for i in range(1,n,2): #1~n-1,間隔2
        s1=s1+f(x[i])
    
    for i in range(2,n-1,2): #2~n-2,間隔2
        s2=s2+f(x[i])
    
    total=(h/3)*(f(a)+4*s1+2*s2+f(b))

    return(total)

def f(x):
    return x**3

#M列表用來裝中點法的誤差
M=list()
T=list()
S=list()
#f(x)定積分(0~1)真解
ture_int=1/4

for n in range(3,18):
    M.append(abs(midpoint_int(0,1,n)-ture_int))
    T.append(abs(trap(0,1,n)-ture_int))
    S.append(abs(simpson(0,1,n)-ture_int))

x=np.linspace(3,8,len(M))
plt.plot(x,M,'r',label='mid point rule error')
plt.plot(x,T,'k',label='trap. rule error')
plt.plot(x,S,'b',label='simpson rule error')
plt.xlabel('n')
plt.ylabel('error')
plt.legend()
plt.show()

