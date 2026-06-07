f = open("D:/ha.txt","r",encoding="utf-8")      # 打开文件

# 方法1
# num = 0
# for line in f.readlines():
#     line = line.strip()     # 去掉开头与结尾换行
#     lst = line.split(" ")   # 按空格分出来单词
#     for word in lst:
#         if word == "itheima":
#             num += 1
# print(num)

# 方法2
num = 0
for line in f.readlines():
    line = line.strip()     # 去掉开头与结尾换行
    num += line.count("itheima")
print(num)

# 方法3
# num = 0
# for line in f.readlines():
#     line = line.strip()     # 去掉开头与结尾换行
#     if "itheima" in line:   # "itheima"是否在line里面，如果在返回Ture，如果一行有多个"itheima"，就没有上面的严谨
#         num += 1
# print(num)

f.close()       # 关闭文件