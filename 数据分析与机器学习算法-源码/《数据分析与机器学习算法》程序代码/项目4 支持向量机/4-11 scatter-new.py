import numpy as np
import matplotlib.pyplot as plt
import time
np.random.seed(int(time.time()))
n = 116
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X)
#产生绘制数据，T为颜色
plt.scatter(X,Y, s=75, c=T, alpha=0.6)
plt.xlim(-1.5,1.5), plt.xticks([])
plt.ylim(-1.5,1.5), plt.yticks([])
plt.show()

