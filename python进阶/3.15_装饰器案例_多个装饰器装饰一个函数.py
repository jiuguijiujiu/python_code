def login(fn_obj):
    def fn_inner():
        print("登录")
        fn_obj()
    return fn_inner

def verify(fn_obj):
    def fn_inner():
        print("验证")
        fn_obj()
    return fn_inner

# @login
# @verify
def comment():
    print("评论")

# comment()

comment = login(verify(comment))
comment()