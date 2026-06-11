# 1. 定义插入排序函数
def select_sort(my_list):
    # 1.1 外层循环影响比较总轮数
    for i in range(1, len(my_list)):        # i = 1     2       3       4
        # 1.2 内循环控制比较次数
        for j in range(i, 0, -1):           # j = 1     2,1     3,2,1   4,3,2,1
            # 比较：如果下标j < j-1元素则交换
            if my_list[j] < my_list[j - 1]: # j-1 =0    1.0     2,1,0   3,2,1,0
                my_list[j], my_list[j - 1] = my_list[j - 1], my_list[j]
            # 否则下标j > j-1元素,说明确定位置跳出循环
            else:
                break


# 2. 测试
if __name__ == '__main__':
    my_list = [5, 3, 4, 7, 2]

    print(f"冒泡排序前：{my_list}")
    print('-' * 50)
    select_sort(my_list)
    print(f"冒泡排序后：{my_list}")