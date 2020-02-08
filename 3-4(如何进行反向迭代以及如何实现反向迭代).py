"""
iter(a)需要a.__iter__方法存在，
reversed(a)需要a.__reversed__存在（该方法会对a进行反向迭代）
实际案例：
要求:
x = ReversedQueue(3,4,0.2)
for i in x:
    print(i)
输出(3.8,3.6,3.4,3.2.3.0)
"""


class FloatRange(object):
    def __init__(self, start, end, step):
        self.start = start
        self.step = step
        self.end = end

    def __iter__(self):
        # 正向迭代
        while self.start <= self.end:
            yield self.start
            self.start += self.step


    def __reversed__(self):
        # 反向迭代
        while self.end >= self.start:
            yield self.end
            self.end -= self.step


if __name__ == '__main__':
    fr = FloatRange(1.0, 4.0, 0.5)
    for i in reversed(fr):
        print(i)