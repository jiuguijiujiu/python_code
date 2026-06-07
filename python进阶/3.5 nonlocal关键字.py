"""
nonlocal关键字的使用
"""

def f_outer():
    num = 100
    def f_inner():
        nonlocal num
        num += 1
        print(f"修改后num = {num}")

    return f_inner

f = f_outer()
f()
f()
f()