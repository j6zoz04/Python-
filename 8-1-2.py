#數值積分-梯型法

import numpy as np

def f(x):
    return x**2

def trap(a,b,n):
    x=np.linspace(a,b,n+1) #x會是一個陣列(array)
    x=np.delete(x,[0,n])
    h=(b-a)/n
    fk=f(x) #列表(list)無法對裡面的元素做數學運算，但陣列(array)可以
    s=h*(0.5*(f(a)+f(b))+sum(fk)) #利用sum函數即可不用for迴圈

    return(s)
    
#積分下限
a=0
#積分上限
b=1
#分段數
n=100

print(trap(a,b,n))