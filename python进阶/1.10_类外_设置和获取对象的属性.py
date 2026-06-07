class Car():
    def run(self):
        print("我会跑")

car = Car()
car.run()

# 类外添加属性
car.color =  "红色"
car.number = 4

print(f"车的颜色是{car.color}")
print(f"车有{car.number}个轮子")
