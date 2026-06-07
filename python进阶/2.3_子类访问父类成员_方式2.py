# 学校类
class School:
    def __init__(self):
        # 会的技能
        self.kongfu = "[黑马学校煎饼果子配方]"

    # 摊煎饼动作
    def make_cake(self):
        print(f"用{self.kongfu}做一个香喷喷的煎饼")


class Prentice(School):
    def __init__(self):
        # 会的技能
        self.kongfu = "[自创煎饼果子配方]"

    # 摊煎饼动作
    def make_cake(self):
        print(f"用{self.kongfu}做一个香喷喷的煎饼")

    def make_School_cake(self):
        super().__init__()   # self.kongfu被改了
        super().make_cake()

xm = Prentice()
xm.make_cake()
xm.make_School_cake()
xm.make_cake()