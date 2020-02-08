"""
如何过滤[1,2,3,-1,-2,-3]中的负数
"""
data = [1, 2, 3, -1, -2, -3]


# 1.filter方法
def filter_data():
    result = filter(lambda x: x > 0, data)
    print(list(result))  # 注意 此处返回的是生成器


if __name__ == '__main__':
    filter_data()
