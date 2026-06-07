"""
类内如何访问类中的函数（行为）,其实用self关键字实现
"""

"""
# 类外用（对象名.函数名）的方式调用
class Car:
    def run(self):
        print("我是车，我会跑！")


car = Car()
car.run()
"""

# 类内调用函数
class Car:
    def run(self):
        print(f"我是{self}车，我会跑！")

    def work(self):
        print(f"我是work函数，我的self是{self}")
        # Car#run()
        self.run()

car = Car()
print(f"car对象:{car}")
# Car#work()
car.work()