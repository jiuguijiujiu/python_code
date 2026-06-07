"""
演示魔法方法__del__()
"""

class Car:
    def __init__(self, brand):
        """
        给汽车类对象的属性初始化
        :param brand: 品牌
        """
        self.brand = brand

    def __str__(self):
        return f'{self.brand}'

    def __del__(self):
        print(f"对象被删除了")


car = Car('BMW')
print(car)

print('-' * 50)

# del car
# print(car) # 报错
print("程序结束")
