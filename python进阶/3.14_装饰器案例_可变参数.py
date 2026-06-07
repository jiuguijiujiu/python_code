"""
装饰器案例——可变参数，且有返回值
"""
def my_decorator(fn_obj):
    def fn_inner(*args, **kwargs):
        print("计算中...")
        return fn_obj(*args, **kwargs)
    return fn_inner


def get_sum(*args, **kwargs):
    """
    求元组与字典里值的和
    :param args:将多个参数打包成元组
    :param kwargs:将多个参数打包成字典
    :return:返回计算结果
    """
    sum = 0
    for arg in args:
        sum += arg

    for v in kwargs.values():
        sum += v

    return sum

    # # 上述代码可以优化如下
    # return sum(args) + sum(kwargs.values())

# print(get_sum(1, 2, 3, a=4, b=5, c=6))
get_sum = my_decorator(get_sum)
print(get_sum(1, 2, 3, a=4, b=5, c=6))