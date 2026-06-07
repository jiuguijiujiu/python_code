"""
演示__init__魔法方法（无参数）
"""

class Car(object):

    def __init__(self):
        self.color = '黑色'
        self.number = 3

    def show(self):
        print(f"车颜色：{self.color}，车轮胎数：{self.number}")

car = Car()
car.show()