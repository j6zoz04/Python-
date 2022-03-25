#Python的矩陣功能
import numpy.linalg as la
import numpy.random as rn
import numpy as np
#亂數製造一個4x4矩陣
#使用np.mat造出來的矩陣可進行四則運算、求反矩陣...等數學操作
A=np.mat(rn.randn(4,4))
print('A=',A)
#亂數製造一個行(column)向量(4x1)
#(row,column)
xt=np.mat(rn.randn(4,1))
print('xt=',xt)
#相乘
b=A*xt
print('b=',b)
#解Ax=b
x=la.solve(A,b)
print('x=',x)
#比較x和xt的誤差
print(la.norm(x-xt))
#整數矩陣
A=np.round(A*10)
print('A=',A)
#矩陣平方
B=A**2
print('B=',B)
#矩陣的行列式值
print('det(A)=',la.det(A))
#製作4x4單位矩陣(Identity Matrix),即I矩陣
C=np.mat(np.identity(4))
print('C=',C)
#矩陣加法
D=C+A
print('D=',D)
#矩陣的秩(Rank)
print('rank(A)=',la.matrix_rank(A))
print('rank(D)=',la.matrix_rank(D))
#抽取子矩陣
#抽取D矩陣左上3X3作為子矩陣
E=D[0:3,0:3]
print('E=',E)
#抽取A矩陣第0行(column 0)
v=A[:,0]
print('v=',v)
#抽取A矩陣第2行(column 2)
u=A[:,2]
print('u=',u)
#矩陣的轉置(Transpose)
print('Transpose(u)=',u.T)
#向量內積(列*行)(row*column)
z=u.T*v
print('z=',z)
#上式內積後仍以矩陣型式呈現，可用float(z)轉成純量(scalar)呈現
z=float(z)
print('float(z)=',z)

