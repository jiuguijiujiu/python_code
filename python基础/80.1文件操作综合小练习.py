fr = open("D:/Temporary_file/bill.txt", "r", encoding="utf-8")
fw = open("D:/Temporary_file/bill正式.txt", "w", encoding="utf-8")

# for line in fr.readlines():
#     if "测试" in line:
#         print(line)
#         continue
#     fw.write(line)

for line in fr.readlines():
    line = line.strip()
    lst = line.split(",")
    if "测试" == lst[4]:
        print(line)
        continue
    fw.write(line + "\n")
    # fw.write("\n")


fr.close()
fw.close()
