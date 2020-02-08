from collections import Counter
from random import randint
import re

"""
场景一：某随机序列[12, 5, 6, 4, 53, 56...]中，找出出现次数最高的三个元素，他们出现次数是多少？
"""

def counter_study():
    data = [randint(0, 20) for x in range(
        30)]  # 得到一个例如[8, 0, 0, 8, 14, 10, 6, 20, 7, 11, 7, 17, 3, 4, 6, 8, 19, 12, 1, 11, 19, 6, 9, 7, 7, 19, 4, 4, 14, 14]的数组

    result = Counter(
        data)  # Counter({7: 4, 8: 3, 14: 3, 6: 3, 4: 3, 19: 3, 0: 2, 11: 2, 10: 1, 20: 1, 17: 1, 3: 1, 12: 1, 1: 1, 9: 1})
    top3_result = result.most_common(3)  # 获取出现频次最高的三个元素 [(17, 3), (14, 3), (15, 3)]
    print(top3_result)


# counter_study()


"""
场景2：对某英文文章的单词，进行词频统计，找到出现次数最高的10个单词，他们出现的次数是多少
"""


def counter_study2():
    text = "hello, i am teacher. my name is ....."
    result = Counter(re.split("\W+", text))
    top3_result = result.most_common(3)
