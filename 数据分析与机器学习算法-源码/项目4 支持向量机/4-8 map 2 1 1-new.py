from pylab import *
subplot(2,2,1)
#产生两行两列的子图，先设置第一个子图
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,1)', ha='center', va='center', size=10,alpha=.5)
subplot(2,2,2)
#设置第二个子图
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,2)',ha='center',va='center', size=13,alpha=1.0)
subplot(2,2,3)
#设置第三个子图
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,3)',ha='center',va='center', size=16,alpha=1.5)
subplot(2,2,4)
#设置第四个子图
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,2,4)',ha='center',va='center', size=20,alpha=2.0)
show()


