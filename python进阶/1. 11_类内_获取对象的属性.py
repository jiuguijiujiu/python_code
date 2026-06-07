class Car():
    def run(self):
        print("我会跑")

    def show(self):
        print(f"车的颜色是{self.color}")
        print(f"车有{self.number}个轮子")

car = Car()
car.run()

# 类外添加属性
car.color =  "红色"
car.number = 4

car.show()

