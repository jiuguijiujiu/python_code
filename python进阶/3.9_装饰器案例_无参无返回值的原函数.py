def my_decorator(fn_obj):
    def fn_inner():
        print("计算中...")
        fn_obj()
    return fn_inner

def get_sum():
    a = 10
    b = 20
    sum = a + b
    print(f"两数之和：{sum}")

get_sum = my_decorator(get_sum)
get_sum()