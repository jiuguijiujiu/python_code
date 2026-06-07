def func(name, age, *args, **kwargs):
    print(f"我是{name}, 年龄{age}岁, 我的爱好有：", end = "")
    for arg in args:
        print(arg, end = " ")

    print(f"\n我的其他信息：", end = "")
    for k in kwargs:
        print(f"{k}:{kwargs[k]}", end = " ")

func("周杰伦", 18, "篮球", "看书", "唱歌", 身高 = 180, 体重 = 160, 偶像 = "刘德华")