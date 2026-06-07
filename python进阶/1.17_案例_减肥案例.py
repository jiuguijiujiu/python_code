class Student:
    def __init__(self, current_weight):
        self.current_weight = current_weight

    def run(self):
        print("跑步")
        self.current_weight -= 0.5

    def eat(self):
        print("大吃大喝")
        self.current_weight += 2

    def __str__(self):
        return f"当前体重{self.current_weight}kg"


xm = Student(100)
print(xm)
xm.run()
print(xm)
xm.eat()
print(xm)