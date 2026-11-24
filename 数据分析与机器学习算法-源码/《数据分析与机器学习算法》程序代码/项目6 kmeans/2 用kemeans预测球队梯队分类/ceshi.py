# 获取数据，使用pandas读取数据
import pandas as pd
#写入文件所在的路径
data = pd.read_csv(r"D:/data.csv",encoding='gb2312')
# 初步打印出数据读取的结果
print(data.head())

# 提取需要进行分析的数据
train_x = data[['2019年国际排名', '2018年世界杯', '2015年亚洲杯']]
df = pd.DataFrame(train_x)

# 数据处理，归一化数据
from sklearn import preprocessing
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)

# 模型训练：利用sklearn中的K-Means算法实现聚类，K=3
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'梯队编号'},axis=1,inplace=True)
print(result.head(19))
print("----------------------------------------------------")
tx = result[['国家','梯队编号']]
# print(tx.head())

# 模型评估后进行绘图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib
# 对字体进行处理
font = {'family': 'simhei',
        'weight': 'bold',
        'size': 10}
matplotlib.rc("font", **font)
# 构建X，Y，Z轴，分别对应每一组数据
xs = data.iloc[:,2]
ys = data.iloc[:,3]
zs = data.iloc[:,4]
fig = plt.figure()
ax=Axes3D(fig)
name = data.iloc[:,1]
for label,x,y,z in zip(name,xs,ys,zs):
    ax.scatter(x,y,z)
    ax.text(x, y, z, label)
cValue = ['r','y','g','b','r','y','g','b','r']
# 对每一条轴命名
ax.set_xlabel('2019年国际排名')
ax.set_ylabel('2018年世界杯')
ax.set_zlabel('2015年亚洲杯')
plt.show()



