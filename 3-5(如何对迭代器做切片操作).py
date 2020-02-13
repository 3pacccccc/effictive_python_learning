"""
实际案例：
有某个文本文件，我们想读取其中某个范围的内容如100-300行之间的内容，
python中文本文件是可迭代对象，我们是否可以使用类似列表切片的方式
得到一个100~300行文件内容的生成器？
"""

from itertools import islice
# 解决方案
with open('a.txt', 'r') as f:
    # 假设a.txt是一个10G大小的文件，要是使用f.readlines()会让内存爆炸，而且我们只想要100-300行的内容
    # for line in islice(f, 100, 300):# 100-300行
    for line in islice(f, 100,None):# 100行到最后
    # for line in islice(f, 500):# 前500行

        print(line)


"""
小结：
for line in islice(f, 100, 300):# 100-300行
这个操作实际上也读取了前面100行的内容，只是被抛弃掉了。而且要是在进行
for i in f操作的话，会从第301行开始
"""