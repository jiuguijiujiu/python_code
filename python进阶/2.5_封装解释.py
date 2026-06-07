"""
封装案例
"""
# 徒弟类
class Prentice():
    def __init__(self):
        # 会的技能（公开）
        self.kongfu = "[xm自创煎饼果子配方]"

        # 私有的属性
        self.__money = 100000

    # 提供私有属性访问接口
    def get_money(self):
        return self.__money

    # 修改金额接口
    def set_money(self, money):
        self.__money = money

    # 摊煎饼动作
    def make_cake(self):
        print(f"用{self.kongfu}做一个香喷喷的煎饼")

# 徒孙类
class Tusun(Prentice):
    pass

if __name__ == '__main__':
    zs = Tusun()

    # 访问师傅的钱
    print(zs.get_money())   # 接口访问（成功）
    # print(zs.__money)         # 直接访问（失败）

    # 接口修改金额
    zs.set_money(100)
    print(zs.get_money())   # 接口访问（成功）

    # 直接修改金额（失败）
    zs.__money = 100000000  # 类外定义
    print(zs.get_money())

