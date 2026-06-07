"""
多进程入门案例

实现方法：
1. 导包
2. 创建进程对象，关联目标函数
3. 启动进程
"""

# 导包
import multiprocessing
import time

# 1. 定义函数 表示 敲代码
def coding():
    for i in range(1,11):
        time.sleep(0.1)     # 模拟耗时操作，更好的观看进程抢资源的效果（多进程执行效果）
        print(f"正在敲第{i}遍代码！")

# 2. 定义函数 表示 听音乐
def music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听第{i}遍音乐。。。")

if __name__ == '__main__':
    # 3. 创建两个进程对象，分别绑定两个目标函数
    # 进程p1关联coding，如果他抢到了cpu资源，他就会执行coding这个函数
    p1 = multiprocessing.Process(target=coding)
    # 进程p2关联music，如果他抢到了cpu资源，他就会执行music这个函数
    p2 = multiprocessing.Process(target=music)

    # 4. 启动进程
    p1.start()
    p2.start()
