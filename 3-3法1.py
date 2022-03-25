#simple iteration Xn+1=g(Xn)
#example:f(x)=e^x-2x-1=0 (求此函數的根)
#=>e^x=2x+1
#=>x=ln(2x+1)=g(x)  (找出滿足此等式的x即為f(x)的根)
#數學上，若找得到一個x*等於g(x*)，則稱x*為固定點，因此此方法又稱定點迭代法
import numpy as np

def g(x):

    return np.log(2*x+1)
#在numpy模組中，函式log預設為ln

tol=10**(-14)
i=0
x0=1
x1=g(x0)

while abs(x1-x0)>tol:
    print(i,x1)
    i=i+1
    x0=x1
    x1=g(x0)