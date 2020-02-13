"""
实际案例：
我们要把某个字符串衣服分割符号拆分不同的字段，该字符串包含多种不同的分隔符，例如：
s = 'ab;cd|ef|hi,jkl|mn\topq;rst,uvw\txyz'
其中,;|\t都是分割符号，如何处理
"""

# 解决方案：采用re.split()方法
import re

s = 'ab;cd|ef|hi,jkl|mn\topq;rst,uvw\txyz'
result = re.split(r'[,;\t|]+', s)

