#數值積分-adaptive quadrature
#使用simpson rule的adaptive quadrature
import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return(400*x*(1-x)*np.exp(-2*x))

def simpson(a,b,n):
    if n%2==0:
        n=n
    else:
        print('非偶數區間，程式將區間+1')
        n=n+1

    h=(b-a)/n
    s1=0
    s2=0

    for i in range(1,n,2): #x1~xn-1,間隔2
        s1=s1+f(a+h*i)
    
    for i in range(2,n-1,2): #x2~xn-2,間隔2
        s2=s2+f(a+h*i)


    total=(h/3)*(f(a)+4*s1+2*s2+f(b))

    return(total)

#下列函式難懂，要查一下遞迴的觀念
def recursive_simpson(a,b,S,tol):
    print('將計算的區間:',a,b)
    #S=simpson(a,b,2)
    i=0
    c=(a+b)/2
    SL=simpson(a,c,2)#SL:右半區間面積
    SR=simpson(c,b,2)#SR:左半區間面積
    err=abs(S-(SR+SL))/15
    if err<=tol:#用來終止遞迴的條件
        S=SR+SL
        nodes=[a,c,b]
        #print('nodes=',nodes)
        return(S,err,nodes)
    else:
        #遞迴:if是flase，繼續把面積切個更細
        SL,err1,nodes1=recursive_simpson(a,c,SL,tol/2)
        print('回傳nodes1=',nodes1)
        #每一次上面的if是flase，便會對那次的區間再對半分一次(再送回recursive_simpson)
        #在SR內形成新的SR和SL
        SR,err2,nodes2=recursive_simpson(c,b,SR,tol/2)
        print('回傳nodes2=',nodes2)
        S=SL+SR
        err=err1+err2
        nodes=nodes1[0:-1]+nodes2
        print('目前總nodes:',nodes)
        return(S,err,nodes)
        
         
        
def adaptive_simpson(a,b,tol=10**(1)):
    s=simpson(a,b,2)
    s,err,nodes=recursive_simpson(a,b,s,tol)
    return(s,err,nodes)
##輸入區##
s,err,nodes=adaptive_simpson(0,10,10**(-1))
########
print('近似面積:',s,'誤差:',err,'分點數:',len(nodes))
x=np.linspace(0,10,200)
plt.plot(x,f(x),'r',label='function f(x)')
x1=np.array(nodes)
y1=np.zeros(len(x1))
plt.plot(x1,y1,'b*',label='points')
plt.legend()
plt.show()
#可看到在函數波動較大的地方會有較多的分割數
#觀察print出來的東西，以便了解遞迴是怎麼走的

    

    


