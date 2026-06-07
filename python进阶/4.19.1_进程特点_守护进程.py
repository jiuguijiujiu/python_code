"""
演示 默认情况下主进程会等待所有子进程全部结束后再结束
"""

# 导包
import multiprocessing
import time

# 1. 定义函数 woke
def woke():
    for i in range(10):
        time.sleep(0.2)
        print("努力工作中。。。")

# 2. 主进程
if __name__ == '__main__':
    # 3. 创建子进程，且给进程取名字
    # 进程创建默认命名方式：process-编号（编号从1开始依次往后）
    p1 = multiprocessing.Process(target=woke, name='woke')
    # print(f"p1_name:{p1.name}")

    # 4. 启动进程
    p1.start()

    # 主进程（main）休眠一秒后结束
    time.sleep(1)
    print("程序结束")

