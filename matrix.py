import numpy as np
import numpy.random as rn
#4-1也有矩陣相關運算
#建立一個可供數學運算的矩陣
A=np.mat([[1,2,3],[4,5,6],[7,8,9]])
print('A=',A)
#取得(row1,column1)元素，注意在Python的index是從0開始
print(A[0,0])
#取得(row2,column3)元素
print(A[1,2])
#取得A左上2X2子矩陣，注意在Python中0:2代表只取2的前一個，即0~1
print(A[0:2,0:2])
#取得A的row1
print(A[0])
#取得A的column2
print(A[:,1])
#取得A的row1及row3
print(A[[0,2]])
#以A的(row1,column1)元素取代A的整個row1及row2->B矩陣
#把A矩陣複製給B矩陣，避免後續運算影響到原來的A矩陣
B=A.copy()
B[[0,1],:]=B[0,0]
print('A=',A)
print('B=',B)
#將A的row2和row1對調->C矩陣
#把A矩陣複製給C矩陣，避免後續運算影響到原來的A矩陣
C=A.copy()
C[[0,1],:]=C[[1,0],:]
print('A=',A)
print('C=',C)
#矩陣A的大小
m,n=A.shape
print('Number of row of A=',m)
print('Number of column of A=',n)
#建立一個3x3的零矩陣，並將A矩陣代入
R=np.mat(np.zeros([m,n]))
R[:,:]=A
print('R=',R)
#
print(A[0,1:])

    


        
    
    
        





        
        
    
    
        


        


    