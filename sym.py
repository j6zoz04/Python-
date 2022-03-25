#Sympy為Python的符號運算模組
import numpy as np
import sympy as sp
from sympy import sin,cos
from sympy import *
#SymPy 的數字格式有 3 種：整數(Integer)、浮點數(Float)、有理數(Rational)，其中有理數是以分數的型式顯示
a,po,s=symbols('a po s')

H=-(a**2*cos(s)**2+po**2*sin(s)**2)*po**2*a**2

L=((po**2-a**2)*cos(s)*sin(s))**2
R=(a**2*cos(s)**2+po**2*sin(s)**2)*(a**2*sin(s)**2+po**2*cos(s)**2)

Q=H/(L-R)
print(Q)
print(simplify(Q))


