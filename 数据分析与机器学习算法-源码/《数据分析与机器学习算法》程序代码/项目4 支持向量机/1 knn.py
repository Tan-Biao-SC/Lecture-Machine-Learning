#引入工具包
import numpy as np
from sklearn.neighbors import KNeighborsClassifier as knn
#定义数据
ar_x=[[4032,1680,1450,5.3,5.6],
      [4330,1535,1885,7.8,14.5],
      [4053,1740,1449,6.2,10.8],
      [5087,1868,1500,8.5,25.6],
      [4560,1822,1645,7.8,15.8],
      [3797,1510,1820,5.5,9.6]]
ar_y=[0,1,0,1]
#利用均一化处理数据
ar_min=np.min(ar_x,0)
ar_mn=np.max(ar_x,0)-ar_min
nor_ar=np.around((ar_x-ar_min)/ar_mn,4)
#print(ar_x)
print(nor_ar)  #打印归一化后的矩阵
#建立模型并预测
model=knn(n_neighbors=3)
model.fit(nor_ar[:4],ar_y)
pre=model.predict(nor_ar[4:6])
print(pre)
