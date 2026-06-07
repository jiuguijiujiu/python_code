"""
创建生成器——yield关键字
"""

# 需求：通过yield，创建生成器之1~10之间整数
# 回顾：生成器表达式
my_gt1 = (i for i in range(1, 11))

# yield写法
# 1. 定义一个函数，存储到生成器中，返回生成器
def my_gt():
    # list = []                 # 创建
    # for i in range(1, 11):
    #     list.append(i)        # 存储
    # return list               # 返回

    # 效果类似于上面代码
    # yield做了三件事：1. 创建生成器对象 2. 将数据存储到生成器中 3. 返回生成器
    for i in range(1, 11):
        yield i

# 2. 测试
my_g = my_gt1
print(type(my_g))

# 获取元素
print(next(my_g))
print(next(my_g))
print('-' * 50)

for i in my_g:
    print(i)