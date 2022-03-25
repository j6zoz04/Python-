#矩陣的列運算(Row operator)
import numpy as np
import numpy.random as rn
#3x3單位矩陣
#np.mat()造出的矩陣可用於各種運算
I=np.mat(np.identity(3))
print('I=',I)

#製造測試矩陣[A]
#np.rand(3,3)用於在1~10取亂數造出3x3矩陣
#np.round()將矩陣每個元素只取整數
A=np.mat(np.round(rn.rand(3,3)*10))
print('A=',A)

#第一種基礎矩陣

#不使用E1=I,而是複製一個I給E1,如此一來當我對E1進行操作皆不會影響到I
E1=I.copy()

#將E1的第2列乘3加到第3列(注意矩陣的index是從0開始)
#後面的冒號":"代表一整列
E1[2,:]=E1[1,:]*3+E1[2,:]
print('E1=',E1)
#將A第2列乘3加到第3列=B矩陣
B=E1*A
print('A=',A)
print('B=',B)


#第二種基礎矩陣
E2=I.copy()
E2[2,:]=E2[2,:]*2
print('E2=',E2)
#將A的第3列乘2=B矩陣
B=E2*A
print('A=',A)
print('B=',B)

#第三種基礎矩陣(兩列對調)
E3=I.copy()
E3[[0,1]]=E3[[1,0]]
print('E3=',E3)
B=E3*A
print('A=',A)
print('B=',B)

