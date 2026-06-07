"""
Property属性_装饰器用法案例
"""

# 需求：定义学生类，设置学生私有属性age，通过Property进行简化调用
# 1. 定义学生类
class Student:
    # 1.1 设置私有属性age
    def __init__(self):
        self.__age = 18

    # 1.2 得到私有age接口
    @property           # @property，装饰获取值函数
    def get_age(self):
        return self.__age

    # 1.3 修改私有age接口
    @get_age.setter     # @获取值函数.setter，装饰修改值函数
    def set_age(self,age):
        self.__age = age

# 测试
s = Student()

# s.set_age(20)
# print(s.get_age())

# 一般property装饰获取值函数与修改值函数可以同名，这里不演示
# 装饰后
s.set_age  = 22
print(s.get_age)