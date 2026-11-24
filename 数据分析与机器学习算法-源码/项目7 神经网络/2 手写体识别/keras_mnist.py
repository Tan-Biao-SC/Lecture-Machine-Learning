"""
keras-minist.py
Created on Sat Aug 14 15:30:32 2021
"""
import numpy as np

from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from tensorflow.keras.optimizers import SGD
import time

np.random.seed(int(time.time()))

# 下载 mnist 数据集 to the path '~/.keras/datasets/'
# 加载数据
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data pre-processing 数据预处理
X_train = X_train.reshape(X_train.shape[0], -1) / 255. #为了简单，都变成一维，normalize
X_test = X_test.reshape(X_test.shape[0], -1) / 255.  #为了简单，都变成一维，normalize
y_train = np_utils.to_categorical(y_train, num_classes=10) #10个数字，下同
y_test = np_utils.to_categorical(y_test, num_classes=10)

#顺序模型，除此之外还有任意模型，支持有向环等拓扑
model = Sequential()
#第一个全连接层，输出32维，输入784
model.add(Dense(32, input_shape = (784,)))
#用relu作为激活函数
model.add(Activation('relu'))
#第二个全连接层输出10
model.add(Dense(10))
#第二层使用softmax 分类
model.add(Activation('softmax'))

#keras的为方便组成网络，对链接矩阵的维度进行了自动计算
 
#定义一个优化方法
sgd=SGD(lr=0.005, momentum=0.0, decay=0.0, nesterov=False)

#为网络配置优化器和损失函数所使用的目标函数，这里为分类器准备了交叉熵函数
model.compile(optimizer=sgd,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
 
print('Training ------------')
model.fit(X_train, y_train, epochs=2, batch_size=64)

print('\nTesting ------------')
loss, accuracy = model.evaluate(X_test, y_test)

print('test loss: ', loss)
print('test accuracy: ', accuracy)