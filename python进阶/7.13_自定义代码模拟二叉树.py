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

