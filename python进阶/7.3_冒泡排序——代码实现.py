# 1. 定义冒泡排序函数
def bubble_sort(my_list):
    # 1.1 外侧循环记录冒泡轮次
    for i in range(len(my_list) - 1):   # i的值：0，1，2，3，4......
        # 细节1：创建一个计数器，记录比较次数
        count = 0
        # 1.2 内层循环记录每轮比较次数
        for j in range(len(my_list) - 1 - i):
            # 1.3 如果前面元素大于后面元素则交换
            if my_list[j] > my_list[j + 1]:
                # 细节2 ： 发生交换，count+1
                count += 1
                # 1.4 交换
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
            # 1.5 如果后面元素大于前面元素则什么也不做
        # 细节3：如果在某一轮中，没发生交换，说明已经排序好了，直接结束程序
        print(f"第{i + 1}轮交换{count}次")
        if count == 0:
            break

# 2. 测试
if __name__ == '__main__':
    # my_list = [5, 3, 4, 7, 2]
    # my_list = [2, 3, 4, 5, 7]
    my_list = [3, 2, 5, 7, 6]

    print(f"冒泡排序前：{my_list}")
    print('-' * 50)
    bubble_sort(my_list)
    print(f"冒泡排序后：{my_list}")
