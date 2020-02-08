"""
实际案例：
某软件要求。从网络抓取各个城市气温信息，并依次显示：
北京：15~20，
天津：17~22，
长春：12~18，
......
如果依次抓取所有城市的天气再显示，显示第一个城市气温时，
有很高的延迟，并且浪费存储空间，我们期望以"用时访问"的策略，
并且能把所有城市气温封装到对象里，用for语句进行迭代，如何解决？
"""

# iter(A)方法会优先访问A.__iter__方法，如果A没有__iter__方法，就会访问A.__getitem__方法!!!

"""
解决方案：
step1: 实现一个迭代器对象WeatherIterator,next方法每次返回一个城市气温
step2: 实现一个可迭代对象WeatherIterable,__iter__方法每次返回一个迭代器对象
"""

import requests
from collections import Iterator, Iterable
import time

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = -1

    def get_weather(self, city):
        time.sleep(3)
        r = requests.get("http://wthrcdn.etouch.cn/weather_mini?city={0}".format(city))
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def __next__(self):
        if self.index == len(self.cities) - 1:
            raise StopIteration
        self.index += 1
        return self.get_weather(self.cities[self.index])


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


if __name__ == '__main__':
    for x in WeatherIterable(['重庆','广州','乌鲁木齐','成都']):
        print(x)
