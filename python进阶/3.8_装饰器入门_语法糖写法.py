"""
装饰器入门_语法糖写法案例
再每个功能前加充值功能
"""

def log_in(f_name):
    def inner():            # 有嵌套
        print("登录")   # 额外功能
        f_name()            # 有引用

    return inner            # 有返回

@log_in             # 语法糖
def comment():
    print("发表评论")

@log_in             # 语法糖
def payment():
    print("充值")



if __name__ == '__main__':
    comment()
    print('-' * 50)
    payment()