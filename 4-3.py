#高斯消去法Gauss elimination
import numpy as np
import numpy.random as rn
#假設A矩陣為非奇異矩陣，且為方陣(反矩陣存在、可逆)
#解Ax=b
def Gauss_elimination(A,b):
    #用shape調出矩陣A的大小
    m,n=A.shape
    #R目前為0矩陣(mxn+1)，用來接下來形成增廣矩陣
    #強制將A的資料改成浮點數，才能浮點運算
    A=A.astype(float)
    ################
    R=np.mat(np.zeros([m,n+1]))
    R[:,:n]=A
    R[:,n]=b
    print('initial R=',R)
    for i in range(m): 
        #i從0~m-1
        #find maximun element in the column i
        maxEc=abs(R[i,i])
        maxRow=i
        for k in range(i+1,m):
            #k從i+1~m-1
            if abs(R[k,i])>maxEc:
                maxEc=R[k,i]
                maxRow=k
        #swap maximun row with current row        
        R[[i,maxRow],i:]=R[[maxRow,i],i:]
        #Make all row below this one to 0
        for k in range(i+1,m):
            c=-(R[k,i])/R[i,i]
            R[k,i:]=R[k,i:]+c*R[i,i:]
    #Upper traingular matrix is finished
    print('Upper traingular R=',R)
    #Now solve equation for an upper traingular matrix
    x=np.mat(np.zeros([m,1]))
    for i in range(m-1,-1,-1):
        #i=m-1~0
        x[i]=R[i,-1]/R[i,i]
        for k in range(i-1,-1,-1):
            R[k,-1]=R[k,-1]-R[k,i]*x[i]
    
    return x
#A
#A=np.mat(np.round(rn.rand(4,4)*10))
A=np.mat([[1,2,3],[0,4,5],[0,0,8]])
print('A=',A)
#xt:真解
#xt=np.mat(np.round(rn.rand(4,1)*10))
#print('Exact solution xt=',xt)
#b
#b=A*xt
b=np.mat([[1],[2],[4]])
print('b=',b)
#x:使用高斯消去法解增廣矩陣[A|b]求得之解
x=Gauss_elimination(A,b)
print('Gauss Elimination solution x=',x)

            

    
            
        

    
