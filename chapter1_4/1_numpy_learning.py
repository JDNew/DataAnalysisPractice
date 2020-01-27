"""
假设一个团队里有 5 名学员，统计下这些人在语文、英语、数学中的平均成绩、最小成绩、最大成绩、方差、标准差。
然后把这些人的总成绩排序，得出名次进行成绩输出。
"""
import numpy as np

person_type = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['U32', 'i', 'i', 'i']
})

people = np.array([('ZhangFei', 66, 65, 30), ('GuanYu', 95, 85, 98),
                   ('ZhaoYun', 93, 92, 96), ('HuangZong', 90, 88, 77),
                   ('DianWei', 80, 90, 90)],
                  dtype=person_type)

chinese = people[:]['chinese']
english = people[:]['english']
math = people[:]['math']
ranking = sorted(people, key=lambda x: x[1] + x[2] + x[3], reverse=True)

# 平均值
print('the average of chinese is %.1f' % np.mean(chinese))
print('the average of english is %.1f' % + np.mean(english))
print('the average of math is %.1f' % + np.mean(math))
# 最大值
print('the max score of chinese is %d ' % np.max(chinese))
print('the max score of english is %d ' % np.max(english))
print('the max score of math is %d ' % np.max(math))
# 最小值
print('the min score of chinese is %d ' % np.min(chinese))
print('the min score of english is %d ' % np.min(english))
print('the min score of math is %d ' % np.min(math))
# 标准差
print('the standard deviation of chinese is %d ' % np.std(chinese))
print('the standard deviation of english is %d ' % np.std(english))
print('the standard deviation of math is %d ' % np.std(math))
# 方差
print('the variance of chinese is %d ' % np.var(chinese))
print('the variance of english is %d ' % np.var(english))
print('the variance of math is %d ' % np.var(math))
# 排名
print(ranking)
