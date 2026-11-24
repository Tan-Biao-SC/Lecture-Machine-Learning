import numpy as np
import matplotlib.pyplot as plt
#让绘图显示汉字
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#各地区名字
name = ['北京','天津','上海','河北','山东','浙江','云南','吉林','广西','宁夏','安徽']
place_count = [60605,54546,45819,28243,13270,9945,7679,6799,6101,4621,20105]
#展现各地区的占比
plt.figure(figsize=(20, 8), dpi=100)
# 通过pie
plt.pie(place_count, labels=name, autopct='%1.2f%%', colors=["#d58930", "#28cfed", "#236be2", "#bd59d5", "#2fcea7", "#ee4a4b", "#0c9cef", "#9999ff", "#ff9999", "#35ad6b", "#a442a0"])
# 指定显示的pie是正圆
plt.axis('equal')
plt.legend(loc='best')
plt.title("各地区占比示意图")
plt.show()
