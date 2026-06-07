"""
使用type查看字面量与变量的类型
"""

# type查看字面量
# 方法1直接print输出
print(type(100))
print(type(2.5))
print(type("周杰伦"))
print("---------------------")

# 方法2先存变量后print输出
int_type = type(100)
float_type = type(2.5)
str_type = type("林俊杰")
print(int_type)
print(float_type)
print(str_type)
print("---------------------")

# type查看变量的类型
name = "周杰伦"
age = 25
height = 178
print(type(name))
print(type(age))
print(type(height))
