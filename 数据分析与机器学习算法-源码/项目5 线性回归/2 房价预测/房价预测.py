from io import StringIO
import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np


def get_data(file_name):
    """
    获取csv数据,给出自变量x,因变量y的list
    :param file_name:
    :return:
    """
    data = pd.read_csv(file_name)
    x, y = [], []
    for i, j in zip(data['square_feet'], data['price']):
        x.append([float(i)])
        y.append(float(j))
    return x, y


def main():
    # 输入文本，为了方便重现，直接将csv文件改为通过StringIO方法输入
    input_data = StringIO(
        'square_feet,price\n150,6450\n200,7450\n250,8450\n300,9450\n350,11450\n400,15450\n600,18450\n')

    # 划分训练集自变量与因变量
    x_train, y_train = get_data(input_data)

    # 创建对象,训练数据，输出回归函数参数
    regr = linear_model.LinearRegression()
    regr.fit(x_train, y_train)
    print("截距：" + str(regr.intercept_))
    print("斜率：" + str(regr.coef_))

    # 两种方式测试结果
    test = [500]
    print(regr.predict(np.array(test).reshape(1, -1)))
    print(500 * regr.coef_ + regr.intercept_)

    # 画图，包括训练集，回归函数和测试结果
    plt.scatter(x_train, y_train, color='blue')
    plt.scatter(test, regr.predict(np.array(test).reshape(1, -1)), color='black')
    plt.plot(x_train, regr.predict(x_train), color='red', linewidth=4)
    plt.show()

if __name__ == '__main__':
    main()

