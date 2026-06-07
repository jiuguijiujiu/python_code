"""
类方法与静态方法
"""

# 定义学生类
class Student:
    # 定义类属性
    school = "黑马程序员"

    # 定义类属性
    @classmethod
    def show1(cls):
        print(f"我是cls：{cls}")       # <class '__main__.Student'>,   cls可写其他
        print("我是类方法")

    # 定义静态方法
    @staticmethod
    def show2():
        print("我是静态方法")

# 测试
if __name__ == '__main__':
    s1 = Student()
    s1.show1()
    print('-' * 50)
    s1.show2()