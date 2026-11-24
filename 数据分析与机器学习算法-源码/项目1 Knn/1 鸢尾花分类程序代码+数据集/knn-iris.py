from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
import mglearn
import numpy as np
from collections import Counter
import pandas as pd


class Knn():
    def __init__(self,k=5):
        self.k = k

    def fit(self,x,y):
        self.x = x
        self.y = y

    def dis(self,instant1, instant2):  # 求欧式距离
        dist = np.sqrt(np.sum((instant1 - instant2) ** 2))
        return dist

    def knn_classfy(self,X,y,test):
        distances = [self.dis(x,test) for x in X]
        kneighbors = np.argsort(distances)[:self.k] #选取前K个邻居
        count = Counter(y[kneighbors]) #记标签的个数
        return count.most_common()[0][0]  #统计出现次数最多的标签
    
    def predict(self,test_x):
        pre = [self.knn_classfy(self.x,self.y,i) for i in test_x]  # 预测的标签集
        return  pre

    def score(self,test_x,test_y):
        pre = [self.knn_classfy(self.x,self.y,i) for i in test_x]  # 预测的标签集
        col = np.count_nonzero((pre == test_y))  # 统计测试集的标签和预测的标签相同的个数
        return col / test_y.size


iris_dataset = load_iris()

x_train, x_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=15)


mknn = Knn(5)
mknn.fit(x_train, y_train)
y_predict = list(mknn.predict(x_test))
print(y_predict)
labels = ["山鸢尾","虹膜锦葵","变色鸢尾"]
for i in range(len(y_predict)):
    print("第%d次测试:真实值:%s\t预测值:%s"%((i+1),labels[y_predict[i]],labels[y_test[i]]))
print("准确率：",mknn.score(x_test, y_test))
