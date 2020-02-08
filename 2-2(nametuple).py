"""
将一个元组的每一个元素命名
"""
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'sex', 'email']) #创建一个元组，每一个元素的名字分别为'name', 'age', 'sex', 'email'

s = Student('jim', 16, 'male', 'jim8721@gmail.com') # 构造一个元组出来,可以直接用s.name,s.age访问元组



