#Power method
import numpy as np
import numpy.random as rn
import numpy.linalg as la

def power_method(A,tol=10**(-12),Maxitr=1000):
    m,n=A.shape
    A=A.astype(float)
    #任意初始向量x0
    x0=np.mat(rn.rand(m,1))
    x0=x0/la.norm(x0)
    x1=(A*x0)/la.norm(A*x0)
    
    i=1
    while la.norm(x1-x0)>tol and i<Maxitr:
        i=i+1
        x0=x1
        x1=(A*x0)/la.norm(A*x0)
        
        if i==Maxitr:
            print('警告,迭代次數超過限制,x1最終結果可能不準確')
    print('總共迭代次數:',i,'次')
    
    L=((A*x1).T*x1)/(x1.T*x1)
    
    return x1,L

#note:輸入的A矩陣必須要為可對角化矩陣
A=np.mat(rn.randn(5,5))
#使得A可對角化(對稱矩陣):A轉置*A
A=np.round(A.T*A*30)
print('A=',A)

x1,L1=(power_method(A))
print('dominant eigen unit vector x1=',x1)
print('dominant eigen value L1=',L1)

#檢查x1是否為eigen vector
b=A*x1
print('b=A*x1=',b)
for i in range(5):
    print('check:b/x1=L1?  ANS:',b[i]/x1[i])


    




