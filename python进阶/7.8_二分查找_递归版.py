"""
二分查找代码_递归
"""

# 1. 定义二分查找函数,递归版本
def binary_search_recursion(my_list, target):
    """
    二分查找函数，确定想查找的值是否在列表里
    :param my_list: 带查找列表
    :param target: 想查找的数据
    :return: Ture说明找到，False说明没找到
    """
    # 1.1 记录列表长度
    n = len(my_list)
    # 1.2 如果列表为空，不用找了，返回false
    if n == 0:
        return False
    # 1.3 获取列表中值
    mid = n // 2
    # 1.4 比较要查找的元素与中值
    if target == my_list[mid]:
        return True
    # 1.5 要查找的值比中值小
    elif target < my_list[mid]:
        return binary_search_recursion(my_list[:mid], target)
    # 1.6 要查找的值比中值大
    else:
        return binary_search_recursion(my_list[mid + 1:], target)

    # 1.7 走到这说明没找到返回false
    return False

# 2. 测试
if __name__ == '__main__':
    my_list = [11, 24, 26, 47, 65, 69, 72, 99, 100]
    print(binary_search_recursion(my_list, 47))
    print(binary_search_recursion(my_list, 11))
    print(binary_search_recursion(my_list, 100))
    print(binary_search_recursion(my_list, 25))
    print(binary_search_recursion(my_list, 1000))
