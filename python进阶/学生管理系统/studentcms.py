"""
学生管理系统的具体实现部分
"""

from student import Student
import time

class StudentCMS:
    def __init__(self):
        # 列表存储学生对象
        self.stu_lst = []
        # self.stu_lst = [
        #     Student("小猫", "女", 18, "111", "喵喵喵"),
        #     Student("小狗", "男", 20, "222", "汪汪汪"),
        #     Student("小猪", "男", 22, "333", "吼吼吼"),
        # ]

    # 系统显示界面
    # 因为函数里没有使用self，所以可以用静态方法
    @staticmethod
    def show_view():
        print('*' * 25)
        print("本系统可完成如下操作：")
        print("\t1.添加学生信息")
        print("\t2.删除学生信息")
        print("\t3.修改学生信息")
        print("\t4.查询学生信息")
        print("\t5.显示所有学生信息")
        print("\t6.保存学生信息")
        print("\t0.退出系统")
        print('*' * 25)

    # 具体功能实现
    # 添加学员信息
    def add(self):
        name = input("请输入学生姓名：")
        gender = input("请输入学生性别：")
        age = int(input("请输入学生年龄："))
        phone = input("请输入学生电话：")
        desc = input("请输入学生描述：")
        # 创建学生对象
        student = Student(name, gender, age, phone, desc)
        print(student)
        # 把对象放入列表里面
        self.stu_lst.append(student)
        print("录入信息成功")

    # 删除学员信息
    def delete(self):
        # 按照输入的名字匹配进行删除
        del_name = input("请输入要删除学生的姓名：")

        for stu in self.stu_lst:
            if stu.name == del_name:
                self.stu_lst.remove(stu)
                print("删除成功")
                break
        else:
            print("没有该学生")

    # 修改学员信息
    def update(self):
        # 按照输入的名字匹配进行修改
        upd_name = input("请输入要修改学生的姓名：")

        for stu in self.stu_lst:
            if stu.name == upd_name:
                stu.gender = input("请输入修改后学生性别：")
                stu.age = int(input("请输入修改后学生年龄："))
                stu.phone = input("请输入修改后学生电话：")
                stu.desc = input("请输入修改后学生描述：")
                print("修改成功")
                break
        else:
            print("没有该学生")

    # 查询单个学员信息
    def search(self):
        # 按照输入的名字匹配进行查询
        search_name = input("请输入要查询学生的姓名：")

        for stu in self.stu_lst:
            if stu.name == search_name:
                print(stu)
                print("查询成功")
                break
        else:
            print("没有该学生")

    # 输出所有学员信息
    def show_all(self):
        # 判断学生列表是否为0，如果为0提示没有信息，不为0则输出
        if len(self.stu_lst) == 0:
            print("没有学生信息")
        else:
            for stu in self.stu_lst:
                # Student有__str__魔法方法，直接输出即可
                print(stu)
            print()

    # 保存学员信息
    def save(self):
        with open('./stu_data.txt', 'w', encoding = 'utf-8') as dest_f:
            stu_dict = [stu.__dict__ for stu in self.stu_lst]
            dest_f.write(str(stu_dict))  # 记得在保存前转为字符串

    # 实现加载学生信息
    def load(self):
        # 加入异常处理，文件可能不存在
        try:
            with open('./stu_data.txt', 'r', encoding = 'utf-8') as scr_f:
                # 读取所有数据
                stu_data = scr_f.read()
                stu_lst = eval(stu_data) # eval()去除双引号，变成列表
                # 如果为空，赋值[]
                if len(stu_lst) == 0:
                    self.stu_lst = []
                # 把字典转为对象放到列表里
                self.stu_lst = [Student(**stu_dict) for stu_dict in stu_lst]
        except:
            # 文件不存在报错则创建
            with open('./stu_data.txt', 'w', encoding='utf-8') as scr_f:
                pass

    # 程序人口
    def start(self):
        # 加载学生数据
        self.load()
        # 循环功能启动
        while True:
            time.sleep(1)
            StudentCMS.show_view()
            num = input("请输入你想操作的序号：")
            if num == '1':
                print("----------1.添加学生信息----------")
                self.add()
            elif num == '2':
                print("----------2.删除学生信息----------")
                self.delete()
            elif num == '3':
                print("----------3.修改学生信息----------")
                self.update()
            elif num == '4':
                print("----------4.查询学生信息----------")
                self.search()
            elif num == '5':
                print("----------5.显示所有学生信息----------")
                self.show_all()
            elif num == '6':
                print("----------6.保存学生信息----------")
                self.save()
                print("保存成功！")
            elif num == '0':
                # 退出时二次验证
                out = input("你确认要退出吗？（y/n）：")
                if out.lower() == "y":  # .lower()把字母转为小写形式
                    self.save()
                    print("退出成功，谢谢你的使用")
                    break
            else:
                print("无效操作，敬请期待")

# 测试
if __name__ == '__main__':
    cms = StudentCMS()
    cms.start()