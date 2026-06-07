# 动物类
class Animal:   # 抽象类（里面有抽象方法，也叫接口）
    def speak(self):    # 抽象方法（没有函数体）
        pass

# 猫类
class Cat(Animal):
    def speak(self):
        print("喵喵")

# 狗类
class Dog(Animal):
    def speak(self):
        print("汪汪")

# 定义函数，接受不同动物对象，调用speak方法
def make_noise(an:Animal):      # an:Animal = cat 父类引用指向子类对象
    an.speak()

if __name__ == '__main__':
    cat = Cat()
    dog = Dog()
    make_noise(cat)
    make_noise(dog)