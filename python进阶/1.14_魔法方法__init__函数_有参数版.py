"""
演示__init__魔法方法（有参数）
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

    def show(self):
        print(self.color, self.number)

car = Car('black', 4)
car.show()