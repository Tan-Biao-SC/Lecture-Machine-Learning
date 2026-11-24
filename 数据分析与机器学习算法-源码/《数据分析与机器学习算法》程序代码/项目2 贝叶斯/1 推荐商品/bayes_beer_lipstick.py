import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB

of = open('beer_lipstick.csv', 'r')
data1 = []
data2 = []
for line in of:
    li_t = line.split(',')
    data1.append([int(li_t[0]), int(li_t[1]), int(li_t[2]), int(li_t[3])])
    data2.append(int(li_t[4]))
cou = int(len(data1)*0.75)
train_x = data1[:cou]
test_x = data1[cou:]
train_y = data2[:cou]
test_y = data2[cou:]

gnb = GaussianNB()
fit1 = gnb.fit(train_x, train_y)
pre = gnb.predict(test_x)
print(pre)
acc_score = gnb.score(test_x,test_y)
print(acc_score)
r_n = (test_y == pre).sum()
print("总测试条数=%d, 贝叶斯正确率=%f%%" % (len(test_x), float(r_n / len(test_x)*100)))

