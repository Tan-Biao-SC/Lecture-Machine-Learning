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
xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1,0,+1] ,[r'$-1$', r'$0$', r'$+1$'])
#xticks和yticks定义X轴和Y轴坐标刻度和标签，第一个参数为刻度，第二个参数为标签
show()
