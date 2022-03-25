#solving triangular system
import numpy as np
import numpy.random as rn
import numpy.linalg as ln

#Forward method
def Forward_method(L,b):
    m,n=L.shape
    x=b.copy()
    for i in range(m):#i=0~m-1
        for k in range(i):#k=0~i-1
            x[i]=x[i]-L[i,k]*x[k]
        x[i]=x[i]/L[i,i]

    return x

def Backward_method(U,y):
    m,n=U.shape
    x=y.copy()
    for i in range(m-1,-1,-1):#i=m-1~0
        for k in range(m-1,i,-1):#k=m-1~i+1
            x[i]=x[i]-U[i,k]*x[k]
        x[i]=x[i]/U[i,i]
    
    return x

def LU(A):
    m,n=A.shape
    #將A的資料轉成浮點(否則如果A都是整數，則接下來A無法使用浮點運算，只會取整數)
    A=A.astype(float)
    ################# 
    U=A.copy()
    L=np.mat(np.identity(m))
    P=L.copy()
    
    for i in range(m): #i=0~m-1
        #find maximum element in the column i
        maxEc=abs(U[i,i])
        maxRow=i
        for k in range(i+1,m): #k=i+1~m-1
            if abs(U[k,i])>maxEc:
                maxEc=U[k,i]
                maxRow=k
        #swap maximum row with current row
        U[[i,maxRow],i:]=U[[maxRow,i],i:]
        P[[i,maxRow],:]=P[[maxRow,i],:]
        L[[i,maxRow],:]=L[[maxRow,i],:]
        L[:,[i,maxRow]]=L[:,[maxRow,i]]

        #print('U=',U)
        for k in range(i+1,m):
            c=-(U[k,i]/U[i,i])
            #print('c=',c)
            #U矩陣:殺掉column i 對角線元素以下的元素(列運算)
            U[k,i:]=U[k,i:]+c*U[i,i:]
            #L矩陣:對應U的行運算算
            L[:,i]=L[:,i]-c*L[:,k]
            #print('U=',U)
    
    return L,U,P

A=np.mat(np.round(rn.rand(4,4)*10))
print('A=',A)
xt=np.mat(np.round(rn.rand(4,1)*10))
print('xt=',xt)

b=A*xt
print('b=',b)

L,U,P=LU(A)
print('P*A=',P*A)
print('L*U=',L*U)

Pb=P*b
print('P*b=',P*b)
#solve Ly=Pb for y
y=Forward_method(L,Pb)
print('y=',y)
#solve Ux=y for x
x=Backward_method(U,y)
print('x=',x)
print('xt=',xt)








    
