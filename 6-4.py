import numpy as np
import numpy.random as rn
def nev(xi,yi,x):
    n=len(xi)
    print('len xi=',len(xi))
    p=[]
    p.append(yi)
    i=0
    while len(p[-1])>1:
        L=[]
        for k in range(n-1):
            #print(k)
            pm=((x-xi[k])*p[-1][k+1]-(x-xi[i+k+1])*p[-1][k])/(xi[i+k+1]-xi[k])
            L.append(pm)
        p.append(L)
            
        i=i+1
        n=n-1
            
    return(p[-1])
#與Lagrange intepolation做個比較
def largrange(xi,yi):
    n=len(xi)
    m=len(yi)
    if n!=m:
        print('xi陣列與yi陣列長度不一致，錯誤的差值點資訊')
    else:
        p=np.poly1d([0]) #初始多項式為0
        for k in range(n): #k=0~n-1
            L=np.poly1d([1]) #初始基底L
            for i in range(n):
                if i!=k:
                    L=L*np.poly1d([1/(xi[k]-xi[i]),-xi[i]/(xi[k]-xi[i])])
                    
            p=p+yi[k]*L #lagrange多項式
    
    return(p) #將largrange多項式回傳





#做出一組差值點
a=20
xi=np.linspace(0,5,a)
yi=rn.randn(a)

r=19
b=nev(xi,yi,xi[r])
c=largrange(xi,yi)
print('實際解:',yi[r])
print('用lagrange多項式算出來的結果:',c(xi[r]))
print('用Nevilles algorithm算出來的結果:',b)
print('lagrange與實際解的誤差=',abs(c(xi[r])-yi[r]))
print('Nevilles algorithm與實際解的誤差=',abs(b[-1]-yi[r]))
#Lagrange和Nevilles在定義域邊界都會有龍格現象，但Lagrange較劇烈
#故Nevilles算出來的結果較準(誤差較小)
#誤差的原因一來是python的問題，二來是算法的問題
#不同的算法就是會有不同的誤差，此為數值分析有趣的地方




            
    

            
            

        



    
    

