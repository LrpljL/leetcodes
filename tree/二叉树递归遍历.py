# coding = utf-8
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(tree):
    if tree is None:
        return
    pre_list.append(tree.val)
    preorder(tree.left)
    preorder(tree.right)


def inorder(tree):
    if tree is None:
        return
    inorder(tree.left)
    in_list.append(tree.val)
    inorder(tree.right)


def postorder(tree):
    if tree is None:
        return
    postorder(tree.left)
    postorder(tree.right)
    post_list.append(tree.val)


if __name__ == "__main__":
    """
[1, 2, 4, 5, 6, 3, 7, 8, 9]
[4, 2, 6, 5, 1, 8, 9, 7, 3]
[4, 6, 5, 2, 9, 8, 7, 3, 1]"""
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    pre_list = []
    preorder(tree)
    print(pre_list)
    in_list = []
    inorder(tree)
    print(in_list)
    post_list = []
    postorder(tree)
    print(post_list)
