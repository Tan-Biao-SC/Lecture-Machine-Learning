from pylab import *
import numpy as np
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
Y = np.sin(X)
plot(X,Y, color="green", linewidth=5.5, linestyle="-",label="Sine")
#定义颜色为绿色，线宽为5.5，线型为实线
#label="***"添加图例
legend(loc="upper left")
xlim(X.min()*1.5,X.max()*1.5)
ylim(Y.min()*1.3,Y.max()*1.3)
#xlim限制X轴的最小值和最大值，ylim限制Y轴的最小值和最大值。
show()
