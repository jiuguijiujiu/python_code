"""
创建汽车对象及访问类中成员
"""

# 定义类，类名遵循大驼峰命名法（首字母大写）
class Car:
    # 定义方法
    def run(self):
        print("我是汽车，我会跑！")

# 创建汽车类对象
car = Car()
# 访问类中成员，调用car#run()
car.run()