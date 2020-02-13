"""
实际案例：
将{
    "a": 12,
    "bwvr": 13,
    "cd": 14,
    "wer": 15,
}
转化为
a   :12,
bwvr:13,
cd  :14,
wer :15,
(居中对齐)
"""

# 方法1：str.ljust(), str.rjust(), str.center()进行左右居中对齐
s = 'abc'
s.ljust(5) # 5为最终字符串的宽度 'abc  '
s.ljust(5, '=') # '='为需要填充的字符串 'abc==' rjust center同理



# 方法2：使用format()方法，传递类似'<20', '>20', '^20'参数完成同样任务
b = 'abc'
format(b, '>5') # 右对齐
format(b, '<5') # 左对齐
format(b, '^5') # 居中对齐


