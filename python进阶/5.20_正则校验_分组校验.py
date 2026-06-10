"""
正则校验_正则校验
"""


import re
# 需求：在列表fruits = {'apple', 'banana', 'pear', 'orange'}匹配apple与pear

fruits = {'apple', 'banana', 'pear', 'orange'}

# 遍历每一个水果
for fruit in fruits:
    # 判断水果是不是apple与pear
    if re.match("apple|pear", fruit):
        print(f"我爱吃：{fruit}")
    else:
        print(f"我不爱吃：{fruit}")