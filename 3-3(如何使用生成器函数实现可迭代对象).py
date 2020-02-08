"""
实际案例：实现一个可迭代对象的类，他能迭代出给定范围内所有的素数:
pn = PrimeNumbers(1,30)
for k in pn:
    print(k)
输出结果：
2 3 5 7......
"""

import time

"""
！！！
经测试，方法test(3.002s)效率远高于PrimeNumbers(87.07)
"""


class PrimeNumbers(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        time.sleep(3)
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end):
            if self.isPrimeNum(k):
                yield k


def test(start, end):
    time.sleep(3)
    result = []
    for i in range(start, end):
        if i < 2:
            continue
        for k in range(2, i):
            if i % k == 0:
                continue
            else:
                if k in result:
                    continue
                result.append(k)
    return result


if __name__ == '__main__':
    start = time.time()
    result = test(1, 30)
    end = time.time()
    print(result)
    print(end - start)
    # pn = PrimeNumbers(1, 30)
    # for i in pn:
    #     end = time.time()
    #     print(i)
    #     print('time cost{0}'.format(end - start))
    #     print('-----------------------------')
