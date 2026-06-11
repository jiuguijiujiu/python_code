# 1. 创建列表结点类
class SingleNode:
    # 1.1 初始化属性
    def __init__(self, item):
        self.item = item    # 数值域
        self.next = None    # 地址域

# 2. 创建列表类
class SingleLinkList:
    # 2.1 初始化属性
    def __init__(self, node = None):
        self.head = node

    # 2.2 is_empty (self) 链表是否为空
    def is_empty(self):
        # 2.2.1 判断头结点是否为None，如果是返回Ture，否则返回False
        return self.head is None

    # 2.3 length (self) 链表长度
    def length(self):
        # 2.3.1 count记录长度（计数器）
        count = 0
        # 2.3.2 cur记录当前位置（游标），从第一个元素开始
        cur = self.head
        # 2.3.3 循环：遍历列表，cur判断有没有到最后一个元素，若到none则为最后一个元素，结束循环，否则移动到下一个元素
        while cur:
            # 2.3.3.1 计数器+1，cur指向下一个元素
            count += 1
            cur = cur.next
        # 2.3.4 返回长度
        return count

    # 2.4 travel (self.) 遍历整个链表
    def travel(self):
        # 2.4.1 游标记录当前位置
        cur = self.head
        # 2.4.2 循环：遍历列表，cur判断有没有到最后一个元素，若到none则为最后一个元素，结束循环，否则移动到下一个元素
        while cur:
            # 2.4.2.1 打印当前元素数据域
            print(f"数据域:{cur.item}")
            # 2.4.2.2 指向下一个元素
            cur = cur.next

    # 2.5 add (self, item) 链表头部添加元素
    def add(self, item):
        # 2.5.1 创建结点类
        new_node = SingleNode(item)
        # 2.5.2 将新元素的链接域指向head指向的元素地址
        new_node.next = self.head
        # 2.5.3 head头结点的链接域指向新元素的地址
        self.head = new_node

    # 2.6 append (self, item) 链表尾部添加元素
    def append(self, item):
        # 2.6.1 创建一个结点类
        new_node = SingleNode(item)
        # 2.6.2判断列表是否为空。若为空，则head直接指向新结点
        if self.is_empty():
            self.head = new_node
        else:
            # 2.6.3 让cur指向最后一个元素
            cur = self.head
            while cur.next:
                cur = cur.next
            # 2.6.4 让最后一个元素（cur）指向新元素
            cur.next = new_node

    # 2.7 insert (self, pos, item) 指定位置添加元素
    def insert(self, pos, item):
        # 2.7.1 pos<=0,则插到列表头部
        if pos <= 0:
            self.add(item)
        # 2.7.2 pos>=self.length()，则插到列表尾部
        elif pos >= self.length():
            self.append(item)
        # 2.7.3 否则插到列表指定位置
        else:
            new_node = SingleNode(item)
            # 2.7.4设置一个游标 以及 设置一个记录游标当前下标的变量
            cur = self.head
            count = 0
            # 2.7.5 cur要到想插入位置的前一个元素那里
            while count < pos-1:
                cur = cur.next
                count += 1
            # 2.7.6 插入
            new_node.next = cur.next
            cur.next = new_node

    # 2.8 remove (self, item) 删除节点
    def remove(self, item):
        # 2.8.1 cur当前指向
        cur = self.head
        # 2.8.2 pre指向前一个元素
        pre = None
        # 2.8.3 循环遍历列表，找到要删除的元素
        while cur:
            # 2.8.4 找到了
            if cur.item == item:
                # 2.8.6 特殊情况删除的是第一个结点
                if cur == self.head:
                    self.head = cur.next
                    # 2.8.7 其他情况
                else:
                    pre.next = cur.next
                # 2.8.8 删除成功直接结束
                return
            # 2.8.5 没找到
            else:
                pre = cur
                cur = cur.next

    # 2.9 search (self, item) 查找节点是否存在
    def search(self, item):
        cur = self.head
        # 2.9.1 遍历列表
        while cur:
            # 2.9.2 找到了返回ture
            if cur.item == item:
                return True
            # 2.9.3 没找到指向下一个元素
            cur = cur.next
        # 2.9.4 每找到，返回false
        return False

# # 3. 测试
# if __name__ == '__main__':
#     # 3.1 测试结点类
#     node1 = SingleNode(10)
#
#     # 3.2 打印当前结点的 元素域 与 链接域
#     print(f"node对象：{node1}的数据域为{node1.item}，地址域为{node1.next}，类型为{type(node1)}")
#
#     # 3.3 测试链表类
#     my_ll = SingleLinkList(node1)
#     print(f"头节点为{my_ll},它指向{my_ll.head}")
#     print(f"第一个元素的元素域：{my_ll.head.item}，链接域：{my_ll.head.next}")


# 4 完整测试
if __name__ == '__main__':
    # 4.1 创建结点类
    node1 = SingleNode("刘备")

    # 4.2 创建链表类，头结点指向node1
    my_ll = SingleLinkList(node1)

    # 4.3 打印第一个元素的 元素域 与 链接域
    print(f"第一个元素的元素域：{my_ll.head.item}，链接域：{my_ll.head.next}")
    print('-' * 50)

    # 4.7 在链首添加新元素
    my_ll.add("关羽")
    my_ll.add("张飞")

    # 4.8 往尾部插入元素
    my_ll.append("孙权")
    my_ll.append("孙策")

    # 4.9 往指定位置插入元素
    my_ll.insert(-3, "曹操")
    my_ll.insert(9, "大乔")
    my_ll.insert(4, "小乔")

    #4.10 删除指定元素
    my_ll.remove("曹操")
    my_ll.remove("小乔")
    my_ll.remove("大乔")

    # 4.4 判空
    print(f"链表是否为空？：{my_ll.is_empty()}")
    print('-' * 50)

    # 4.5 计算列表长度
    print(f"链表长度：{my_ll.length()}")
    print('-' * 50)

    # 4.6 遍历列表
    my_ll.travel()
    print('-' * 50)

    # 4.11 查看元素在不在列表里面
    print("张飞在列表里吗？：%s" % my_ll.search("张飞"))
    print("曹操在列表里吗？：%s" % my_ll.search("曹操"))
