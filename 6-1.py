#差值法介紹、python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.interpolate import lagrange

x=np.linspace(-2*np.pi,np.pi,200)
y=2*np.sin(x)-3*np.cos(x)

xi=np.linspace(-2*np.pi,np.pi,6)
yi=2*np.sin(xi)-3*np.cos(xi)

f=interp1d(xi,yi,kind='cubic')

#ynew=f(x)
plt.plot(xi,yi,'k')
plt.show()