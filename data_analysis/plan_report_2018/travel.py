"""
2018计划完成情况分析 -- 出游
"""

from matplotlib import pyplot as plt

num_per_month = [4, 1, 3, 2, 3, 1, 0, 1, 2, 2, 0, 0]
with_children = [1, 1, 2, 2, 2, 1, 0, 0, 1, 1, 0, 0]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

num_past_month = []
num_past_month.append(num_per_month[0])
for month in range(1, len(num_per_month)):
    num_past_month.append(num_per_month[month] + num_past_month[month - 1])

# 数据可视化
# print(num_past_month)
plt.figure(1)
p1 = plt.bar(months, num_per_month, color='SkyBlue', label='Total')
p2 = plt.bar(months, with_children, color='orange', label='With Children')

plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
plt.title(u'每月交际/出游次数 - 2018', color='676767', fontsize=16)
plt.xlabel(u"月份", color='676767', fontsize=12)
plt.ylabel("", fontsize=12)
plt.legend()

plt.figure(2)
plt.plot(months, num_past_month, '-o', ms=15, lw=2, alpha=0.7, mfc='orange')
plt.grid()

plt.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
plt.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
plt.title(u'交际/出游累计次数 - 2018', color='676767', fontsize=16)
plt.xlabel(u"月份", color='676767', fontsize=12)
plt.ylabel("", fontsize=12)

plt.show()