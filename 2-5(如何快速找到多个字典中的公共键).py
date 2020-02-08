"""
实际案例：
西班牙足球甲级联赛，每轮球员进球统计：
第一轮：{'苏亚雷斯'：1，'梅西'：2， '本泽马'：3}，
第2轮：{'苏亚雷斯'：1，'梅西'：2， '本泽马'：3}，
第3轮：{'苏亚雷斯'：1，'梅西'：2， '本泽马'：3}，
统计出前N轮，每场比赛都有进球的球员
"""
from random import randint, sample

# sample('abcdef', N) # 从abcdef中随机抽取N个
round_1 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}  # 随机产生每轮的进球球员跟进球数
round_2 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}  # 随机产生每轮的进球球员跟进球数
round_3 = {x: randint(1, 4) for x in sample('abcdef', randint(3, 6))}  # 随机产生每轮的进球球员跟进球数

# 方法1：
result_1 = round_1.viewkeys() & round_2.viewkeys() & round_3.viewkeys()  # 将所有的集合取交集

# 方法2：使用map, reduce方法
result_2 = reduce(lambda a, b: a & b, map(dict.viewkeys, [round_1, round_2, round_3]))
