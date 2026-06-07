"""
生成器推导式写法
"""
import sys      # 导入system系统模块

# 场景1:生成器推导式写法
# 需求1：生成1~10之间的整数
my_generator = (i for i in range(1, 11))
print(my_generator)
print(type(my_generator))
print('-' * 50)

# 需求2：1~10之间的偶数
my_gt2 = (i for i in range(1, 11) if i % 2 == 0)
print(my_gt2)
print('-' * 50)

# 需求3：如何从生成器中获取数据
# 方法1：next（）
print(next(my_gt2)) # 2
print(next(my_gt2)) # 4
print('-' * 50)

# 方法2：for循环
for i in my_gt2:
    print(i)        # 6 8 10
print('-' * 50)

# 验证：生成器的目的就是减少内存占用
my_list = [i for i in range(1000000)]
my_gt3 = (i for i in range(1000000))
print(type(my_list), type(my_gt3))

# 查看my_list与my_gt3的内存占用情况
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_gt3))