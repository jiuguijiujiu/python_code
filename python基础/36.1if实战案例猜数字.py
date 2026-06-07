import random
num = random.randint(1, 10)

num2 = int(input("请输入第一次数字："))

if num2 == num:
    print("猜对了")
else:
    if num2 > num:
        print("大了")
    if num2 < num:
        print("小了")

    num2 = int(input("请输入第二次数字："))
    if num2 == num:
        print("猜对了")
    else:
        if num2 > num:
            print("大了")
        if num2 < num:
            print("小了")

        num2 = int(input("请输入第三次数字："))
        if num2 == num:
            print("猜对了")
        else:
            print("算了告诉你吧，数字是：%d" % num)