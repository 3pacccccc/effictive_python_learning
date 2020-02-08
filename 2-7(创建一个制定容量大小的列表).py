from collections import deque

# deque可以指定列表的大小，如果超出了大小，会挤出去最先进来的元素(FIFO),一般用来用作历史记录等功能

history = deque([], 5)  # 创建一个指定大小为5的数组

history.append(1)  # history = [1]
history.append(2)  # history = [1,2]
history.append(3)  # history = [1,2,3]
history.append(4)  # history = [1,2,3,4]
history.append(5)  # history = [1,2,3,4,5]
history.append(6)  # history = [2,3,4,5, 6] #最先进来的1被挤出去，数组一直保持大小为5
