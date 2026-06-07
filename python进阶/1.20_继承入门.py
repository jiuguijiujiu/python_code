"""
子类继承父类
"""

class Father:
    def __init__(self):
        self.sex = "男"

    def walk(self):
        print("我喜欢散步")

    def smoke(self):
        print("吸烟有害健康")

class Son(Father):
    pass

son = Son()
print(son.sex)
son.walk()
# 耦合性 
son.smoke()