#牛頓法
#試著解f(x)=e^x-2x-1的根
#並驗證牛頓法是否真的是二次收斂(c是否會收斂到一個常數)?
import numpy as np

#定義原函數
def f(x):
    return np.exp(x)-2*x-1
#定義切線斜率
def df(x):
    return np.exp(x)-2
#初始值
x0=-1
#迭代次數值
i=0
#收斂誤差
tol=10**(-14)
#建立一個空的列表
c=[]

while abs(f(x0))>tol:
    i=i+1
    x1=x0-f(x0)/df(x0)
    en=x1-x0
    c.append(abs(x1)/abs(x0)**2)
    x0=x1
    print(i,x1,'en=',en,[c[i-1]])

print('將迭代後的根代回f(x)，其值為f(x0)=',f(x0))