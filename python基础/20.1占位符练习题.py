money = 100
name = "周杰伦"
salary = 500.10

message = "我叫%s，钱包有%d元，但是今天发了工资%.2f元，目前钱包有%.2f元。" % (name, money, salary, money + salary)
print(message)