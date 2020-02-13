"""
实际案例：
某软件的log文件，其中的日期格式为'yyyy-mm-dd':
......
2016-02-23 werqrew
2016-02-23 werqrew
2016-02-23 werqrew
2016-02-23 werqrew
......
把所有的2016-02-23替换为mm/dd/yyyy格式
"""

import re

# 解决方案：使用re.sub函数
result_1 = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', log)  # log为log日志文件，str格式 \1表示第一组即年

# 也可以为每一组分别命名
result_2 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', log)

