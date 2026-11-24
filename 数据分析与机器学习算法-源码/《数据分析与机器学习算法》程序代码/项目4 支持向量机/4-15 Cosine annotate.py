from pylab import *
import numpy as np
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
S = np.cos(X)
plot(X,S, color="red", linewidth=2.5, linestyle="-",label="Cosine")
#label=”****”添加图例
legend(loc="upper left")
xlim(X.min()*1.2,X.max()*1.2)
ylim(S.min()*1.2,S.max()*1.2)
xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
yticks([-1,0,+1] ,[r'$-1$', r'$0$', r'$+1$'])
ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
t=1*np.pi/2
plot([t,t],[0,np.cos(t)], color ='red', linewidth=2.5, linestyle="--")
scatter([t,],[np.cos(t),], 50, color ='red')
annotate(r'$\cos(\frac{1\pi}{2})=0$',
        xy=(t, np.cos(t)),  xycoords='data',
    xytext=(+10, +30), textcoords='offset points',
    fontsize=16,
arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))
#绘制特殊的点，用annotate函数，第一个参数为显示的内容，xy参数为箭头尖端坐标，xytext参数为文字最左边起始坐标，xycoords坐标系，arrowprops箭头类型
show()
