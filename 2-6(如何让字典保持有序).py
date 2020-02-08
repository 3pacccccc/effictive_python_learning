"""
实际案例：
某编程竞赛系统,对参赛选手编程解题进行计时，选手完成题目后，把该选手解题用时记录到字典中，以便赛后按选手名查询成绩
result = {'a':(2,43), 'b':(1, 23), 'c':(3, 55)}
如何让result变得有序？
"""

# 使用collections.OrderedDict，会像list.append方法一样，先进先出FIFO
from collections import OrderedDict

d = OrderedDict()
d['b'] = ('1', 23)
d['a'] = ('2', 43)
d['c'] = ('3', 55)

d = {'b': (1, 23), "a": (2, 43), 'c': (3, 55)} # d为先进先出的有序字典
