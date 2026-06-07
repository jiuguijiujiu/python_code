"""
with open() as f:
    print(f.readline())
运行完自动调用f.close
"""

with open("D:/ha.txt", "r", encoding = "utf-8") as f:
    for line in f:
        print(line.strip())