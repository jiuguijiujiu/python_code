# 定义类
class Phone(object):
    # 开机方法
    def open(self):
        print("手机能正常开机")

    # 关机方法
    def close(self):
        print("关机，睡觉啦")

    # 拍照方法
    def take_photo(self):
        print("我超自恋，就爱自拍")

# 创建对象并调用方法
phone = Phone()
phone.open()
phone.take_photo()
phone.close()