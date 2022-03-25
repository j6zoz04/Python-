#Inverse Power Method
import numpy as np
import numpy.random as rn
import numpy.linalg as la
###調用4-5的程式(LU分解、Forward Method、Backward Method)###
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
####以下為5-1範圍####
def inverse_power_method(A,mu,tol=10**(-12),Maxitr=10000):
    m,n=A.shape
    A=A.astype(float)
    B=A-mu*np.identity(m)
    y0=np.mat(rn.rand(m,1))
    y0=y0/la.norm(y0)
    L,U,P=LU(B)
    Y=Forward_method(L,P*y0)
    y1=Backward_method(U,Y)
    y1=y1/la.norm(y1)
    i=0
    while la.norm(y1-y0)>tol and abs(la.norm(y1-y0)-2)>tol and i<Maxitr:
        i=i+1
        y0=y1
        Y=Forward_method(L,P*y0)
        y1=Backward_method(U,Y)
        y1=y1/la.norm(y1)
        if i==Maxitr:
            print(y1-y0)
            print('警告,迭代次數超過給定限制,y1最終結果可能不準確')
    print('總共迭代次數:',i,'次')
    L=((A*y1).T*y1)/(y1.T*y1)

    return y1,L

#以下為輸入區:    
#note:輸入的A矩陣必須要為可對角化矩陣
A=np.mat(rn.randn(5,5))
#使得A可對角化(對稱矩陣):A轉置*A
A=np.round(A.T*A*30)
print('A=',A)

#使用python內建計算特徵值的函數
a=la.eig(A)
print('特徵值理論解:L_Theory=',a[0])
###
#自訂mu要靠近哪一個特徵值
mu=100
#
y1,L=inverse_power_method(A,mu)
print('inverse power method特徵向量數值解:y1=',y1)
print('inverse power method特徵值數值解:L=',L)





    
    
