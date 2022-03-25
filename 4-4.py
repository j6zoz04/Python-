#高斯消去法-LU分解
import numpy as np
import numpy.random as rn

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

        print('U=',U)
        for k in range(i+1,m):
            c=-(U[k,i]/U[i,i])
            print('c=',c)
            #U矩陣:殺掉column i 對角線元素以下的元素(列運算)
            U[k,i:]=U[k,i:]+c*U[i,i:]
            #L矩陣:對應U的行運算算
            L[:,i]=L[:,i]-c*L[:,k]
            print('U=',U)
    
    return L,U,P

#A=np.mat(np.round(rn.rand(5,5)*10))
A=np.mat([[4,3,-1],[-2,-4,5],[1,2,6]])
print('A=',A)

L,U,P=LU(A)

print('L=',L)
print('U=',U)
print('P=',P)

print('P*A=',P*A)
print('L*U=',L*U)






    