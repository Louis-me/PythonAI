# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_csv("data1.csv", encoding='GB18030')
# 处理数据
data = df.values.tolist()
times = []  # 记录时间
# score = []
l1 = []
for i in data:
    times.append(i[5])
    # score.append(i[6])
    l1.append(1)

# 设置高度
plt.subplot(711)
# 生成饼图
plt.bar(times, l1, color='black')
plt.yticks([])
plt.xticks([])
plt.show()
