# 1. 定义选择排序函数
def select_sort(my_list):
    # 1.1 外层循环确定比较总轮次，len(my_list) - 1是因为确定n-1个最小的，那剩下的一定是最大的
    for i in range(len(my_list) - 1):
        # 1.2 变量记录最小值下表索引
        min_index = i
        # 1.3 内层循环比较未排序的元素，确定最小值，把最小值放到排序好的队列后，i + 1是因为不用和自己比
        for j in range(i + 1, len(my_list)):
            # 1.4 如果找到最小值，则将min_index指向最小值元素索引
            if my_list[min_index] > my_list[j]:
                min_index = j
        # 1.5 确定最小值，则替换位置
        if min_index != i:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

# 2. 测试
if __name__ == '__main__':
    my_list = [5, 3, 4, 7, 2]

    print(f"冒泡排序前：{my_list}")
    print('-' * 50)
    select_sort(my_list)
    print(f"冒泡排序后：{my_list}")