#牛頓差值法
import numpy as np
import numpy.random as rn
#除式差分
def Divided_difference(xi,yi):
    m=len(xi)
    n=len(yi)
    if m!=n:
        return(print('xi與yi長度需一致'))
    else:
        i=0
        L=list()
        L.append(list(yi))
        while len(L[-1])>1:
            R=list()
            for k in range(len(L[-1])-1):
                d=(L[-1][k+1]-L[-1][k])/(xi[k+1+i]-xi[k])
                R.append(d)
            L.append(R)
            i=i+1
    return(L)

def q(x):
    return x**3+3*x**2-7

xi=np.array(range(10))
yi=q(xi)
L=Divided_difference(xi,yi)
print('xi=',xi)
print('yi=',yi)

for i in range(10):
    print('L',i,'=',L[i])

#每一個L的第一個值即為牛頓差值多項式之係數

        


