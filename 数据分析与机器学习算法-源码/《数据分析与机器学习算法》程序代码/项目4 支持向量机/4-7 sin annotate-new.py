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
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
#设置右和顶部脊柱为无色
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
#设置底部和左脊柱的位置为数据0点
t=3*np.pi/4
plot([t,t],[0,np.sin(t)], color ='red', linewidth=5.5, linestyle="--")
scatter([t,],[np.sin(t),], 60, color ='red')
annotate(r'$\sin(\frac{3\pi}{4})=\frac{\sqrt{2}}{2}$',
        xy=(t, np.sin(t)),  xycoords='data',
    xytext=(+10, +30), textcoords='offset points',
    fontsize=16,
arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
#绘制特殊的点，用annotate函数，第一个参数为显示的内容，xy参数为箭头尖端坐标，xytext参数为文字最左边起始坐标，xycoords坐标系，arrowprops箭头类型
show()

