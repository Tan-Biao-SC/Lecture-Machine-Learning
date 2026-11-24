import numpy as np
import matplotlib.pyplot as plt
import time
np.random.seed(int(time.time()))
N=7
x=np.random.rand(N)
y=np.random.rand(N)
plt.subplot(1,2,1).plot(x[0:2],y[0:2],"bs-")
plt.subplot(1,2,1).plot(x[1:3],y[1:3],"g--")
plt.subplot(1,2,1).plot(x[2:4],y[2:4],"r-")
plt.subplot(1,2,1).plot(x[3:5],y[3:5],"c-.")
plt.subplot(1,2,1).plot(x[4:6],y[4:6],"m:")
plt.subplot(1,2,1).plot(x[5:7],y[5:7],"y*--")
plt_s2=plt.subplot(1,2,2)
plt_s2.plot(x,y,"b-")
#在两个子图内各自绘画
plt.show()



