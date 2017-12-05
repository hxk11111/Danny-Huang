# encoding=utf-8
# 用python实现二叉树，以及实现前序，中序和后序的遍历

class Node(object):
    # 定义节点类
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self, root):
        self.root = root

    def search(self, node, parent, data):
        if node is None:
            return False, node, parent
        if node.data == data:
            return True, node, parent
        if node.data > data:
            return self.search(node.lchild, node, data)
        else:
            return self.search(node.rchild, node, data)

    def insert(self, data):
        flag, n, parent = self.search(self.root, self.root, data)
        if not flag:
            node = Node(data)
            if data > parent.data:
                parent.rchild = node
            else:
                parent.lchild = node

    def delete(self, data):
        flag, n, parent = self.search(self.root, self.root, data)
        if not flag:
            print "Error, could not find such element"
        else:
            if n.lchild is None:
                if n == parent.lchild:
                    parent.lchild = n.rchild
                else:
                    parent.rchild = n.rchild
                del n
            elif n.rchild is None:
                if n == parent.lchild:
                    parent.lchild = n.lchild
                else:
                    parent.rchild = n.lchild
            else:
                right = n.rchild
                if right.lchild is None:
                    n.data = right.data
                    n.rchild = right.rchild
                else:
                    pre = right.lchild
                    while pre.lchild is not None:
                        right = pre
                        pre = pre.lchild
                    n.data = right.data
                    right.lchild = pre.rchild
                    del pre

    def forward_traversal(self, node):
        print node.data
        if node.lchild:
            self.forward_traversal(node.lchild)
        if node.rchild:
            self.forward_traversal(node.rchild)

    def middle_traversal(self, node):
        if node is not None:
            self.middle_traversal(node.lchild)
            print node.data
            self.middle_traversal(node.rchild)


root = Node(10)
t = Tree(root)
t.insert(8)
t.insert(4)
t.insert(18)
t.insert(9)
t.insert(5)
t.insert(15)
t.insert(34)
t.insert(1)
t.delete(5)
t.forward_traversal(t.root)
print "----" * 5
t.middle_traversal(t.root)
