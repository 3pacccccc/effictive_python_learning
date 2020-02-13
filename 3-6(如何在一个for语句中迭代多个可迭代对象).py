"""
实际案例:
1.某班学生期末考试成绩，语文，数学，英语分别存储在3个列表中，
同时迭代三个列表，计算每个学生的总分(并行)。
2.某年级有4个班，某次考试每班英语成绩分别存储在4个列表中，
依次迭代每个列表，统计全学年高于90分人数(串行)。
"""
from random import randint
from itertools import chain


# 解决方案
def solve_1():
    """
    使用zip函数，可以使得zip([1,2],['a','b'])得到[(1,'a'),(2,'b')]
    :return:
    """
    math = [randint(60, 100) for _ in range(40)]  # 随机产生班内每个学生的数学成绩
    chinese = [randint(60, 100) for _ in range(40)]  # 随机产生班内每个学生的语文成绩
    english = [randint(60, 100) for _ in range(40)]  # 随机产生班内每个学生的英语成绩

    total = []
    for c, m, e in zip(chinese, math, english):
        total.append(c + m + e)
    return total


def solve_2():
    """
    问题2的解决方案：使用itertools下的chain函数，可以使得chain([1,2,3],[2,3,4])得到[1,2,3,2,3,4]进行循环
    :return:
    """
    class_1 = [randint(60, 100) for _ in range(35)]  # 随机产生1班的成绩成绩
    class_2 = [randint(60, 100) for _ in range(35)]  # 随机产生2班的成绩成绩
    class_3 = [randint(60, 100) for _ in range(35)]  # 随机产生3班的成绩成绩

    count = 0
    for i in chain(class_1, class_2, class_3):
        if i > 90:
            count += 1
    return count
 