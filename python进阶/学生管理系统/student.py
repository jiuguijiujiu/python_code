"""
该文件记录学生类
"""

class Student:
    # 学生属性
    def __init__(self, name, gender, age, phone, desc):
        """
        初始化学生休息
        :param name: 姓名
        :param gender: 性别
        :param age: 年龄
        :param phone: 电话号码
        :param desc: 描述
        """
        self.name = name
        self.gender = gender
        self.age = age
        self.phone = phone
        self.desc = desc

    def __str__(self):
        """
        打印学生信息
        :return: 学生信息
        """
        return (f"姓名：{self.name}    性别：{self.gender}    年龄：{self.age}   "
                f"电话：{self.phone}   描述：{self.desc}")

# 测试
if __name__ == '__main__':
    s = Student("小明", "男", 18, '100', "篮球")
    print(s)