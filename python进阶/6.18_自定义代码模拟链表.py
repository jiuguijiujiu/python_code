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
        pass

    # 2.7 insert (self, pos, item) 指定位置添加元素
    def insert(self, pos, item):
        pass

    # 2.8 remove (self, item) 删除节点
    def remove(self, item):
        pass

    # 2.9 search (self, item) 查找节点是否存在
    def search(self, item):
        pass

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


    # 4.4 判空
    print(f"链表是否为空？：{my_ll.is_empty()}")
    print('-' * 50)

    # 4.5 计算列表长度
    print(f"链表长度：{my_ll.length()}")
    print('-' * 50)

    # 4.6 遍历列表
    my_ll.travel()