"""
演示闭包写法
"""
# 外部函数
def f_outer(num1):
    # 内部函数
    def f_inner(num2):            # 有嵌套
        num = num1 + num2       # 有引用
        print(f"num = {num}")

    return f_inner                # 有返回

f = f_outer(100)
f(200)

print('-' * 50)

f_outer(100)(400)