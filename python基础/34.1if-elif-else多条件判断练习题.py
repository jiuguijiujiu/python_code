num = 10

if int(input("请输入第一次猜想的数字：")) == num:
    print("猜对了")
elif int(input("不对，再猜：")) == num:
    print("猜对了")
elif int(input("不对，再猜最后一次：")) == num:
    print("猜对了")
else:
    print("好吧告诉你，我的数字是%d" % num)