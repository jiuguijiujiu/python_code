# 练习题
money = 100
name = "刘德华"
salary = 100.99

# ()表示内部的内容是整体，哪怕换行
message = ("我是" + name + "，钱包有" + str(money) +
           "元，但是今天发了工资" + str(salary) + "元，目前钱包有" +
           str(money + salary) + "元。")

print(message)

