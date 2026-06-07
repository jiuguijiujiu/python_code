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


class Prentice(Master, School):
    def __init__(self):
        # 会的技能
        self.kongfu = "[自创煎饼果子配方]"

    # 摊煎饼动作
    def make_cake(self):
        print(f"用{self.kongfu}做一个香喷喷的煎饼")

    def make_Master_cake(self):
        Master.__init__(self)   # self.kongfu被改了
        Master.make_cake(self)

    def make_School_cake(self):
        School.__init__(self)   # self.kongfu被改了
        School.make_cake(self)

xm = Prentice()
xm.make_cake()
xm.make_Master_cake()
xm.make_School_cake()
xm.make_cake()