"""
已知列表: my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd'], 删除所有的bb元素，尽可能多的用不同的解决方案做．
"""
import copy

my_list = ['aa', 'bb', 'cc', 'bb', 'bb', 'bb', 'dd']

# 这样写my_list修改后位置会变，导致错误
# for i in my_list:
#     if i == 'bb':
#         my_list.remove(i)
#
# print(my_list)

# 这样写是my_list[:]切片的意思相当于浅拷贝，就等于拷贝了一份，原my_list变化，和my_list[:]无关，他还保持拷贝的样子
for i in my_list[:]:
# for i in copy.copy(my_list):
    if i == 'bb':
        my_list.remove(i)

print(my_list)