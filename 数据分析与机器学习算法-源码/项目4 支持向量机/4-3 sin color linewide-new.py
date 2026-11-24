from pylab import *
import numpy as np
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
Y = np.sin(X)
plot(X,Y, color="green", linewidth=5.5, linestyle="-",label="Sine")
#定义颜色为绿色，线宽为5.5，线型为实线
#label="***"添加图例
legend(loc="upper left")
show()






