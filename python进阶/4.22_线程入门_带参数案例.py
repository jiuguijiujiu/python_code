"""
多线程完成多任务——带参数版，线程入门案例：一边听音乐一边写代码
"""

# 导包
import threading
import time

# 1. 定义函数 写代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)             # 模拟耗时操作，观看线程抢资源的过程（抢进程抢到的cpu资源）
        print(f"{name}正在写第{i}遍代码")

# 2. 定义函数 听音乐
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐")

# 3. 主程序
if __name__ == '__main__':
    # 4. 创建线程对象，绑定目标函数
    t1 = threading.Thread(target=coding, args=("小明", 10))
    t2 = threading.Thread(target=music, kwargs={'name':"周杰伦", 'count':5})

    # 5. 启动线程
    t1.start()
    t2.start()