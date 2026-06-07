def logging(flag):
    def my_decorator(fn_obj):
        def fn_inner(a, b):
            if flag == '+':
                print("加法计算中")
            elif flag == '-':
                print("减法计算中")
            return fn_obj(a, b)
        return fn_inner
    return my_decorator

@logging('+')
def add(a, b):
    return a + b

@logging('-')
def reduce(a, b):
    return a - b

# 语法糖格式
print(add(3, 4))
print('-' * 50)
print(reduce(3, 4))


