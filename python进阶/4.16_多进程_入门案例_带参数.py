"""
演示带参数多进程案例

进程传参有两种方式：
1. args：接收所有的 位置参数
2. kwargs：接收所有的 关键字参数
"""

# 导包
import multiprocessing, time

# 1. 定义函数 写代码
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)
        print(f"{name} 编写第 {i} 遍代码！")

# 2. 定义函数 听音乐
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)
        print(f"{name} 在听第 {i} 首歌......")

# 3. 创建主进程（主线程）
if __name__ == '__main__':
    # 4. 创建两个子进程，关联上述两个目标函数
    p1 = multiprocessing.Process(target = coding, args = ("大大怪", 10))
    p2 = multiprocessing.Process(target = music, kwargs = {'count':20, 'name':"小小怪"})

    # 5. 启动子进程
    p1.start()
    p2.start()
