"""
正则表达式手机号案例
"""

# 需求：检验手机号（1，长度必须11位 2，纯数字 3，第1位数字必须是1 4，第2位数字是3~9
import re
import string

result = re.match('^1[3-9]\d{9}$', '13245678910')

if result:
    print(result.group())
else:
    print("未匹配")