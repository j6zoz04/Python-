#使用二分逼近法找出f(x)=e^x-2x-2的根
#其中e^x、-2x、-2皆為連續函數，故它們的組合也會是連續函數，可使用二分法
#引用numpy模組
import numpy
#引用numpy中的小模組:random
import numpy.random as rn

#定義函數
def f(x):
    a=numpy.exp(x)-2*x-2
    return(a)

a=1
b=2
c=(a+b)/2   

#設定誤差
tol=10**(-8)

#i用來記錄次數
i=0
while abs(f(c))>tol:
    if f(a)*f(c)<0:
        b=c
        c=(a+b)/2
    elif f(a)*f(c)>0:
        a=c
        c=(a+b)/2
    else:
        pass
    i=i+1
    print(i,c)


print(f(c))

