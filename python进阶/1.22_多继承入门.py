# 师傅类
class Master:
    def __init__(self):
        # 会的技能
        self.kongfu = "[古法煎饼果子配方]"

    # 摊煎饼动作
    def make_cake(self):
        print(f"用{self.kongfu}做一个香喷喷的煎饼")

# 学校类
class School:
    def __init__(self):
        # 会的技能
        self.kongfu = "[黑马学校煎饼果子配方]"

    # 摊煎饼动作
    def make_cake(self):
        print(f"用{self.kongfu}做一个香喷喷的煎饼")


class Prentice(Master, School): # 如果多继承父类的内容有重复，则用就近原则
    pass

xm = Prentice()
print(f"我有{xm.kongfu}")
xm.make_cake()

print('-' * 50)

print(Prentice.mro())