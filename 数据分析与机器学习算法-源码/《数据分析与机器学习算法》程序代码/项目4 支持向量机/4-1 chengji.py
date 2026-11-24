# coding:utf-8
# 导入 tree 模型
import numpy as np
from sklearn.svm import SVC

# 准备数据
of = open('svm_score.csv','r')
x = []
y = []

for line in of:
    li_t=line.split(',')
    # 用60分二值化标记数据
    if(int(li_t[-1]))>=60:
        y.append(1)
    else:
        y.append(-1)
    x.append([float(li_t[0]), float(li_t[1])])
# 关闭文件
of.close()
# 确定训练数据的边界
fd = int(len(x) * 0.8)
# 构造SVM模型

M_svm =SVC(kernel="linear")
M_svm.fit(x[:fd], y[:fd])
# 预测
res = M_svm.predict(x[fd:])

# 计算正确率
ar = (res == y[fd:]) + 0
print("Ar=%.2f%%" % (100.0 * sum(ar) / len(ar)))

w = M_svm.coef_
b = M_svm.intercept_

print (w)
print (b)
