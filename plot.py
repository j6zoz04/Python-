#Python的繪圖模組
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-2*np.pi,2*np.pi,300)
plt.plot(x,np.sin(x))

#使用show()顯示圖表
plt.show()
#使用legend()顯示圖例
plt.legend()
#xlabel('name'):x軸標籤
plt.xlabel()
plt.ylabel()
#plt.subplot(row,column,locate):設定子圖(將多張圖放同一張)
plt.subplot()
#plt.title():圖表標題
plt.title()



 







    