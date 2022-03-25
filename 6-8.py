#差值法:B Spline(樣條差值法)
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

def f(x):
    return 1/(1+x**2)

#差值點
xi=np.linspace(-5,5,13)
yi=f(xi)

#原函數f(x)
x=np.linspace(-5,5,400)
y=f(x)
plt.subplot(3,1,1)
plt.ylabel('f(x)')
plt.xlabel('x')
plt.plot(x,y,'r',label='Initial Function f(x)')
plt.plot(xi,yi,'o',label='Interpolation Point')

#Linear Spline
s1=interp1d(xi,yi,kind='linear')
#Cubic Spline
s3=interp1d(xi,yi,kind='cubic')

y1=s1(x)
y3=s3(x)
plt.plot(x,y1,'c',label='Linear spline')
plt.plot(x,y3,'k',label='Cubic spline')
plt.legend()

R1=list()
R3=list()
p=14
for i in range(4,p):
    xii=np.linspace(-5,5,i)
    yii=f(xii)
    xx=np.linspace(-5,5,400)
    yy=f(xx)
    s11=interp1d(xii,yii,kind='linear')
    s33=interp1d(xii,yii,kind='cubic')
    y11=s11(xx)
    y33=s33(xx)
    e1=max(np.abs(yy-y11))
    e3=max(np.abs(yy-y33))
    R1.append(e1)
    R3.append(e3)
    print(i,R1[-1],R3[-1])

plt.subplot(3,1,3)
plt.title('Linear spline vs Cubic spline')
plt.xlabel('Number of interpolation point')
plt.ylabel('Log(Error)')
plt.plot(np.log(R1),'k',label='Linear spline')
plt.plot(np.log(R3),'r',label='Cubic spline')

plt.legend()
plt.show()


