"""
实际案例：
我们想自定义一种新类型的元组，对于传入的可迭代对象，我们只保留其中int类型且值大于0的元素，例如：
IntTuple([1,'a',-1, 'xbd', ['x', 1], 6, 3]) => (1, 6, 3)
"""

# 解决方案：调用类的__new__方法
class IntTuple(tuple):
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)


if __name__ == '__main__':
    s = IntTuple([1,'a',-1, 'xbd', ['x', 1], 6, 3])
    print(s)