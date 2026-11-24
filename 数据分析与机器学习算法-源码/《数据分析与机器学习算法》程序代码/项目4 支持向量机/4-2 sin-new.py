from pylab import *
import numpy as np
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
Y = np.sin(X)
#产生绘图数据X，Y，为X轴和Y轴一一对应的数据
plot(X,Y)
#以默认的形式绘制数据，plot第一个参数为X坐标数据
#第二个参数为Y坐标数据
show()