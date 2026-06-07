"""
数据类型转换演示
"""

#数字转字符串
t1 = str(123)
print(type(t1))
t2 = str(123.123)
print(type(t2))

#整数与浮点数互转
print(float(123))
print(int(123.123))

#字符串转数字
print(type(int("123")))
print(int("123"))
print(type(float("123.123")))
print(float("123.123"))