"""
文件打开，读写，关闭
"""

f = open("D:/ha.txt", "r", encoding = "utf-8")

# content = f.read()
# print(content)

# content = f.read(3)
# print(content)

# lst = f.readlines()
# print(lst)

# for line in f.readlines():
#     line = line.strip()     # 去除字符串空格与换行
#     print(line)

print(f.readline().strip())
print(f.readline().strip())

f.close()