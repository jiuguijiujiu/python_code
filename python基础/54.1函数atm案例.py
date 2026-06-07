money = 5000000
name = input("请输入你的姓名：")

def check(title):
    """
    查询余额功能
    :return: None
    """
    if title:
        print("-" *10 + "查询余额" + "-" *10)
    print(f"{name}，你好，你的余额是：{money}元。")

def deposit():
    """
    存款功能
    :return: None
    """
    global money
    print("-" * 10 + "存款" + "-" * 10)
    num = int(input("请输入存款金额："))
    print(f"{name}，你好，你存入{num}元成功")
    money += num
    check(False)

def withdrawal():
    """
    取款功能
    :return: None
    """
    global money
    print("-" * 10 + "取款" + "-" * 10)
    num = int(input("请输入取款金额："))
    if num > money:
        print("余额不足")
        check(False)
    else:
        print(f"{name}，你好，你取出{num}元成功")
        money -= num
        check(False)

def menu():
    """
    菜单界面
    :return: 功能选项i
    """
    print("-" * 10 + "主菜单" + "-" * 10)
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入你的选择："))


while True:
    i = menu()
    if i == 1:
        check(True)
    elif i == 2:
        deposit()
    elif i == 3:
        withdrawal()
    else:
        print("欢迎下次光临")
        break