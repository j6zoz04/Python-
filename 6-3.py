#Hermite Interpolation
#Hermite interpolation除了需給定差值點，還需要差值點的導數
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
def f(x):
    return(1/(1+x**2))

#導函數
def df(x):
    return(-2*x/(1+x**2)**2)

def hermite(x,y,z): #z即為差值點倒數y'
    n=len(x)
    m=len(y)
    s=len(z)
    if n!=m!=s:
        print('錯誤的差值點資訊')
    else:
        P=np.poly1d([0])
        for k in range(n):
            L=np.poly1d([1])
            #L
            for i in range(n):
                if k!=i:
                  L=L*np.poly1d([1/(x[k]-x[i]),-x[i]/(x[k]-x[i])])
            #L的微分
            dL=np.polyder(L)
            #H(X)
            H=(np.poly1d([1])-2*dL(x[k])*np.poly1d([1,-x[k]]))*L**2
            #G(X)
            G=np.poly1d([1,-x[k]])*L**2
            #P
            P=P+H*y[k]+G*z[k]
    
    return(P)
#自訂差值點、差值點的導數
xi=np.linspace(-5,5,8)
yi=f(xi)
zi=df(xi)
p=hermite(xi,yi,zi)
#原函數(用來比較)
x=np.linspace(-5,5,200)
y=f(x)
z=df(x)


plt.plot(xi,yi,'o',label='interpolation point')
plt.plot(x,f(x),'b',label='initial function')
plt.plot(x,p(x),'r',label='hermite')
plt.legend()
plt.show()


            
                
