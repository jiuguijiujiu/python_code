"""
演示单任务，前面任务不执行完毕，后面任务绝对不能执行
"""

# 输出10次hello
def hello():
    for i in range(10):
        print("hello")

# 输出10次world
def world():
    for i in range(10):
        print("world")

hello()
print("-" * 50)
world()