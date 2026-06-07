class  SweetPotato:
    # 烤地瓜的属性（时间，状态，调料）
    def __init__(self):
        self.cook_time = 0
        self.state = "生的"
        self.condiments = []

    # 烤地瓜的时间，从而得到状态
    def cook(self, time):
        self.cook_time += time
        if 0 <= self.cook_time < 3:
            self.state = "生的"
        elif 3 <= self.cook_time < 5:
            self.state = "半生不熟"
        elif 7 <= self.cook_time < 12:
            self.state = "熟了"
        else:
            self.state = "烤焦了，糊了"

    # 添加了什么调料
    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f"这个地瓜被烤了{self.cook_time}分钟，状态是{self.state}，调料有{self.condiments}。"

if __name__ == '__main__':
    sweetpotato = SweetPotato()
    print(sweetpotato)

    sweetpotato.cook(8)
    sweetpotato.add_condiment("油")
    sweetpotato.add_condiment("糖")
    print(sweetpotato)

    sweetpotato.add_condiment({"辣椒", "奶酪"})
    sweetpotato.cook(5)
    print(sweetpotato)


