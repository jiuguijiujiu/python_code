"""
property属性——类属性方法
"""

# 需求：定义学生类，设置学生私有属性age，通过Property进行简化调用
# 1. 定义学生类
class Student:
    # 1.1 设置私有属性
    def __init__(self):
        self.__age = 18

    # 1.2 定义得到age入口
    def get_age(self):
        return self.__age

    # 1.3 定义修改age入口
    def set_age(self, age):
        self.__age = age

    # 1.4 封装上述方式为类属性
    age = property(get_age, set_age)

# 2. 测试
if __name__ == '__main__':
    s = Student()
    s.age = 23
    print(s.age)
