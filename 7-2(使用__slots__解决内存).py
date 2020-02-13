"""
对比两个类，一个类设置了__slots__属性，一个没有设置的内存差距
"""

class Player1(object):
    def __init__(self, uid, name, status = 0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


class Play2(object):
    __slots__ = ['uid', 'name', 'status', 'level']
    def __init__(self, uid, name, status = 0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


"""
对比dir(Player1)和dir(Player2)发现，player1多了__dict__属性和__weakref__属性。
主要占内存的就是__dict__属性(占用了1024个字节，是player1用来使用动态绑定属性的功能)
"""