#牛頓法
#試著解f(x)=e^x-2x-2的根
import numpy as np

#定義原函數
def f(x):
    return np.exp(x)-2*x-2
#定義切線斜率
def df(x):
    return np.exp(x)-2
#初始值
x0=1
#迭代次數值
i=0
#收斂誤差
tol=10**(-14)

while abs(f(x0))>tol:
    i=i+1
    x1=x0-f(x0)/df(x0)
    x0=x1
    print(i,x1)

print('將迭代後的根回f(x)，其值為f(x0)=',f(x0))


