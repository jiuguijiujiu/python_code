"""
二分查找代码_非递归
"""

# 1. 定义递归函数
def binary_search(my_list, target):
    # 1.1 开始min，结束max变量
    min = 0
    max = len(my_list)-1
    # 1.2 循环查找，只要没满足情况就一直找
    while min <= max:
        # 1.3 设置min中间值
        mid = (max+min)//2
        if my_list[mid] == target:
            return True
        elif target < my_list[mid]:
            max = mid - 1
        else:
            min = mid + 1
    # 1.4 走到这说明没找到
    return False



# 2. 测试
if __name__ == '__main__':
    my_list = [11, 24, 26, 47, 65, 69, 72, 99, 100]
    print(binary_search(my_list, 47))
    print(binary_search(my_list, 11))
    print(binary_search(my_list, 100))
    print(binary_search(my_list, 25))
    print(binary_search(my_list, 1000))