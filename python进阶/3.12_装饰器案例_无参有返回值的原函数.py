def my_decorator(fn_obj):
    def fn_inner():
        print("计算中...")
        return fn_obj()
    return fn_inner

def get_sum():
    a = 10
    b = 20
    return a + b

get_sum = my_decorator(get_sum)
print(f"两数和为{get_sum()}")