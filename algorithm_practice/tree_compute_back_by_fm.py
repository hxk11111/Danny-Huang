# encoding=utf-8
# 根据一棵树的前序和中序遍历求它的后序遍历
# 前序遍历:GDAFEMHZ, 中序遍历:ADEFGHMZ，求后序遍历

class Node():
    def __init__(self, data=-1, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

def compute_b_by_fm(forward, middle):
    if len(middle) == 1:
        return Node(middle)
    if len(middle) == 0:
        return None
    if len(forward) == 1:
        return Node(forward)
    if len(forward) == 0:
        return None
    root_data = forward[0]
    root = Node(root_data)
    for i in range(len(middle)):
        if root_data == middle[i]:
            lchild_middle = middle[0:i]
            rchild_middle = middle[i+1:]
            lchild_forward = forward[1:i+1]
            rchild_forward = forward[i+1:]
            root.lchild = compute_b_by_fm(lchild_forward, lchild_middle)
            root.rchild = compute_b_by_fm(rchild_forward, rchild_middle)
    return root

def back_traversal(node):
    if node is not None:
        back_traversal(node.lchild)
        back_traversal(node.rchild)
        print node.data


forward = "GDAFEMHZ"
middle = "ADEFGHMZ"
tree_root = compute_b_by_fm(forward, middle)
back_traversal(tree_root)
