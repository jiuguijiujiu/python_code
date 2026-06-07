def my_decorator(fn_obj):
    def fn_inner(a, b):
        print("计算中...")
        return fn_obj(a, b)
    return fn_inner

def get_sum(a, b):
    return a + b

get_sum = my_decorator(get_sum)
print(f"两数和为{get_sum(10, 20)}")