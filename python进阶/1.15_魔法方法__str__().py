"""
演示魔法方法__str__()的使用
"""

class Car:
    def __init__(self, color, number):
        """
        给汽车类对象的属性初始化
        :param color: 颜色
        :param number: 轮胎数
        """
        self.color = color
        self.number = number


    # def show(self):
    #     print(self.color, self.number)

    def __str__(self):
        return f"颜色：{self.color}, 轮胎数{self.number}"


car = Car('black', 4)
# car.show()
print(car)

print('-' * 50)

car1 = Car('red', 6)
# car.show()
print(car1)