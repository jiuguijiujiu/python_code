"""
自定义代码模拟二叉树
"""

# 1. 定义二叉树节点，Node类
class Node:
    # 1.1 初始化属性
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

# 2. 自定义二叉树类，BinaryTree
class BinaryTree:
    # 2.1 初始化属性
    def __init__(self, note = None):
        self.root = note

    # 2.2 定义add函数：添加节点
    def add(self, item):
        pass

    # 2.3 定义广度优先遍历breath函数（逐层遍历）
    def breath(self):
        pass

    # 2.4 定义preorder函数：表示深度优先之先序遍历
    def preorder(self):
        pass

    # 2.5 定义inorder函数：表示深度优先之中序遍历
    def inorder(self):
        pass

    # 2.6 定义postorder函数：表示深度优先之后序遍历
    def postorder(self):
        pass

# 3. 编写测试函数，用于测试对应功能
# 3.1 定义dm01_函数测试节点与二叉树类
def dm01_函数测试节点与二叉树类():
    # 3.1.1 创建节点类
    node1 = Node('A')
    # 3.1.2 打印节点的属性
    print(f"数据：{node1.item}，左子树：{node1.lchild}，右子树：{node1.rchild}")
    print('-' * 50)
    # 3.1.3 创建二叉树类
    # bt = BinaryTree()
    bt = BinaryTree(node1)
    # 3.1.4 打印根节点
    # print(bt.root)
    print(bt.root)
    print(bt.root.item)



# 4. 在main函数中具体测试
if __name__ == '__main__':
    dm01_函数测试节点与二叉树类()