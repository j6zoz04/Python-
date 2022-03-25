#Largrange Interpolation
#6-2 part1
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt

#defined f(x)=2x+log(x)+5sin(x)
def f(x):
    return 2*x+2*np.log(x)+5*np.sin(x)

x=np.linspace(1,20,20)
xx=np.linspace(1,20,100)
y=f(x)
yy=f(xx)

# plt.plot(x,y,'k',xx,yy,'r')
# plt.show()

#poly1d函數:快速製造多項式
# p1=np.poly1d([1,1])
# p2=np.poly1d([2,3])
# print(p1)
# print(p2)
#多項式可四則運算
# p3=p1*p2
# print(p3)

def largrange(xi,yi):
    n=len(xi)
    m=len(yi)
    if n!=m:
        print('xi陣列與yi陣列長度不一致，錯誤的差值點資訊')
    else:
        p=np.poly1d([0]) #初始多項式為0
        for k in range(n): #k=0~n-1
            L=np.poly1d([1]) #初始基底L
            for i in range(n):
                if i!=k:
                    L=L*np.poly1d([1/(xi[k]-xi[i]),-xi[i]/(xi[k]-xi[i])])
                    
            p=p+yi[k]*L #lagrange多項式
    
    return(p) #將largrange多項式回傳


a=largrange(x,y)

plt.plot(x,y,'o',label='f(x) 20pts')
plt.plot(xx,yy,'k',label='f(x) 100pts')
plt.plot(xx,a(xx),'r',label='largrange 10pts')

print(abs(a(x[5])-y[5]))

plt.legend()
plt.show()


