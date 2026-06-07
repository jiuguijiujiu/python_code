"""
演示自定义迭代器
"""

# 需求：模拟rang(1, 5)，自定义 迭代器 实现同等逻辑
# 场景一：rang（）用法
for i in range(1, 5):
    print(i)
print('-' * 50)

# 场景二：自定义迭代器
# 1. 自定义迭代器类
class MyIterator:
    # 1.1 传入参数,通过__init__魔法方法，初始化属性，确定范围
    def __init__(self, star, end):
        self.current_value = star       # 记录当前值，默认开始值
        self.end = end                  # 记录结束值

    # 1.2 重写__iter__魔法方法，返回当前对象（即：迭代对象）
    def __iter__(self):
        return self

    # 1.3 重写__next__魔法方法，返回当前值，更新当前值
    def __next__(self):
        # 1.3.1 判断当前值范围是否合法，
        if self.current_value >= self.end:
            raise StopIteration         # 抛出异常，直接结束迭代

        # current_value = self.current_value
        # self.current_value += 1
        # return current_value
        # 代码等同如下(只用两行)
        self.current_value += 1
        return self.current_value - 1

# 2. for循环遍历
for i in MyIterator(1, 5):
    print(i)
print('-' * 50)

# 3. next()函数
my_list = MyIterator(10, 13)
print(next(my_list))        # 10
print(next(my_list))        # 11
print(next(my_list))        # 12