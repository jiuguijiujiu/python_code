"""
递归入门案例
"""

# 案例1：递归入门案例
# count = 0
#
# def show():
#     global count
#     count += 1
#     if count >= 100:
#         return          # 递归出口
#     print(f"我是show函数：第{count}层递归")
#     show()              # 自己调用自己就是递归

# 案例2：求阶乘
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)



# 测试
if __name__ == '__main__':
    # show()
    num = int(input("请输入你要求的阶乘数："))
    print(factorial(num))