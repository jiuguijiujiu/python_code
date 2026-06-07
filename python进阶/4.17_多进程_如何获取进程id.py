"""
演示如何获取进程id与进程父id
"""

# 导包
import multiprocessing, time, os

# 1. 定义函数 写代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f"{name} 编写第 {i} 遍代码！")
    print(f"p1进程pid：{os.getpid()}|{multiprocessing.current_process().pid}，父进程id(ppid)：{os.getppid()}")

# 2. 定义函数 听音乐
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f"{name} 在听第 {i} 首歌......")
    print(f"p2进程pid：{os.getpid()}|{multiprocessing.current_process().pid}，父进程id(ppid)：{os.getppid()}")



# 3. 创建主进程（主线程）
if __name__ == '__main__':
    # 4. 创建两个子进程，关联上述两个目标函数
    p1 = multiprocessing.Process(target = coding, args = ("大大怪", 10))
    p2 = multiprocessing.Process(target = music, kwargs = {'count':20, 'name':"小小怪"})

    # 5. 启动子进程
    p1.start()
    p2.start()

    # 6. 查看主进程信息
    print(f"main进程pid：{os.getpid()}|{multiprocessing.current_process().pid}，父进程id(ppid)：{os.getppid()}")
