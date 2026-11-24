import numpy as np
import matplotlib.pyplot as plt
n=10
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
plt.axes([0.025,0.025,0.95,0.95])
plt.bar(X,+Y1,facecolor='#13eac9',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
for x,y in zip(X,Y1):
    plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')
#在柱状图的顶部绘制文本，前两个参数为坐标，第三个参数为显示数值
for x,y in zip(X,Y2):
    plt.text(x,-y-0.05,'%.2f'%y,ha='center',va='top')
plt.xlim(-.5,n),plt.xticks([])
plt.ylim(-1.25,+1.25),plt.yticks([])
plt.show()

