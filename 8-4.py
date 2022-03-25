#數值積分
#Gaussian Quadrature
import numpy as np
#N=n+1
def legendre(N):
    if N==0:
        c=np.array([1])
    elif N==1:
        c=np.array([1,0])
    else:
        a=list(legendre(N-1))
        a.append(0)
        a=np.array(a)
        b=list(legendre(N-2))
        L=[0,0]
        L.extend(b)
        L=np.array(L)
        c=((2*N-1)*a-(N-1)*L)/N
    
    return(c)
    
def root_and_weight(N):
    #c:legendre polynomial的係數
    #p:legendre polynomial
    #xi:root of legendre polynomial
    #d:legendre polynomial導函數係數
    #dp:legendre polynomial的導函數
    c=legendre(N)
    p=np.poly1d(c)
    xi=p.r
    xi=np.array(xi)
    print('積分點xi:',xi)

    d=np.polyder(p)
    dp=np.poly1d(d)
    w=2/((1-xi**2)*dp(xi)**2)
    print('權重weight:',w)

    return(xi,w)

def gauss(a,b,N):
    #a,b:積分上下限
    #N:要取幾個積分點
    xi,w=root_and_weight(N)
    xi=(a+b)/2+(b-a)*xi/2
    
    fxi=f(xi)*(b-a)/2
    s=np.dot(fxi,w)
    return(s)
#定義多項式函數    
def f(x):
    return 5*x**4

#進行高斯積分
s=gauss(0,1,5)
print('高斯積分結果:',s)



    

        
    

    






