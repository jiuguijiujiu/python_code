"""
字符串%占位格式化
"""

name = "周杰伦"
age = 18
height = 1.75

# %s占位，可以将原来数字类型自动转为字符串
message = "我叫%s，今年%s岁，身高%s米。" % (name, age, height)
print(message)

# 最好对应占位类型
message = "我叫%s，今年%d岁，身高%.2f米。" % (name, age, height)
print(message)
