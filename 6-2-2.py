#6-2 part2
#largrange多項式的龍格現象(Roungh phe.)
import numpy as np
import numpy.random as rn
import matplotlib.pyplot as plt
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
                    
            p=p+yi[k]*L
    
    return(p)



def f(x):
    return(1/(1+x**2))

# n=15
# x=np.linspace(-5,5,n)
# xx=np.linspace(-5,5,200)
# a=largrange(x,f(x)) #n個差值點的lagrange多項式 
#將差值點n設到10個以上,即可觀察到明顯的龍格現象
#龍格現象主要是因為我們取點都是等間距取點(linspace)，導致在邊界處差值多項式會爛掉
# plt.plot(x,f(x),'o',label='f(x) 10pts')
# plt.plot(xx,f(xx),'k',label='f(x) 200pts')
# plt.plot(xx,a(xx),'r',label='largrange 10pts interpolate')
# plt.legend()
# plt.show()

#畫出Largrange多項式的基底
xi=np.array(range(-4,5))
print(xi)
yi=np.zeros(9)
yi[4]=1
print(yi)

b=largrange(xi,yi)
x=np.linspace(-4,4,200)

plt.plot(x,b(x),'r',label='lagrange 9pts')
plt.plot(xi,yi,'o',label='initial function')
plt.legend()
plt.show()
