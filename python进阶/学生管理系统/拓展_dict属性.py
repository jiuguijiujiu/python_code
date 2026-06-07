"""
演示__dict__，dict将对象变为字典
"""

from student import Student

s1 = Student("小猫", "女", 18, "111", "喵喵喵")
s2 = Student("小狗", "男", 20, "222", "汪汪汪")
stu_list = [s1, s2]
# print(stu)

# dict将对象变为字典
# my_dict = stu.__dict__
# print(my_dict)
# print(type(my_dict))

# 列表推导式
list_dict = [stu.__dict__ for stu in stu_list]
print(list_dict)

# 等同于下面代码
# list_dict = []
# for stu in stu_list:
#     list_dict.append(stu.__dict__)
# print(list_dict)

# 把字典转为对象
my_dict = {'name': '小猫', 'gender': '女', 'age': 18, 'phone': '111', 'desc': '喵喵喵'}
s3 = Student(my_dict['name'], my_dict['gender'], my_dict['age'], my_dict['phone'], my_dict['desc'])
print(s3)
print(type(s3))

# 效果等同上面代码一样
s4 = Student(**my_dict)
print(s4)