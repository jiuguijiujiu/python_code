def my_decorator(fn_obj):
    def fn_inner(a, b):
        print("计算中...")
        fn_obj(a, b)
    return fn_inner

def get_sum(a, b):
    sum = a + b
    print(f"两数之和：{sum}")

get_sum = my_decorator(get_sum)
get_sum(10, 20)