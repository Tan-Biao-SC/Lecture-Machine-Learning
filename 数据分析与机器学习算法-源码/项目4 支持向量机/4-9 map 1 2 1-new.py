from pylab import *
subplot(1,2,1)
#产生一行两列的子图，设置第一个，第一个参数为多少行，第二个参数为多少列，第三个为当前子图
xticks([]), yticks([])
text(0.5,0.5, 'subplot(1,2,1)', ha='center', va='center', size=24,alpha=.5)
subplot(1,2,2)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(1,2,2)', ha='center', va='center', size=24, alpha=.5)
show()
