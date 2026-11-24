from pylab import *
axes([0.1,0.1,.8,.8])
xticks([]), yticks([])
text(0.6,0.7, 'axes([0.1,0.1,.8,.8,hello])',ha='center',va='center',size=20,alpha=.5)
axes([0.2,0.2,.4,.4])
xticks([]), yticks([])
text(0.5,0.5, 'axes([0.2,0.2,.3,.3,ok])',ha='center',va='center',size=16,alpha=.5)
show()

