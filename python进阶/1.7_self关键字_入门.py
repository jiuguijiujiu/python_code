"""
探索self是什么
"""

# 定义类，类名遵循大驼峰命名法（首字母大写）
class Car:
    # 定义方法
    def run(self):
        print(f"self是{self}")
        print("我是汽车，我会跑！")

# 创建汽车类对象1
car1 = Car()
print(f"输出car1对象名：{car1}")
# print(f"car1的地址值：{id(car1)}")
# 调用Car#run()
car1.run()

print("-" * 100)

# 创建汽车类对象2
car2 = Car()
print(f"输出car2对象名：{car2}")
# print(f"car2的地址值：{id(car2)}")
# 调用Car#run()
car2.run()