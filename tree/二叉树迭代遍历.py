# coding = utf-8
"""借助栈或者队列来实现
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder(tree):
    stack_list = []
    pre_list = []
    stack_list.append(tree)
    while stack_list:
        res = stack_list.pop()
        pre_list.append(res.val)
        if res.right:
            stack_list.append(res.right)
        if res.left:
            stack_list.append(res.left)
    return pre_list


def inorder(tree):
    stack_list = []
    in_list = []
    # stack_list.append(tree)
    while stack_list or tree:
        while tree:
            stack_list.append(tree)
            tree = tree.left
        res = stack_list.pop()
        in_list.append(res.val)
        if res.right:
            tree = res.right
    return in_list


def postorder(tree):
    stack_list = []
    post_list = []
    stack_list.append(tree)
    while stack_list:
        tree = stack_list.pop()
        if tree.left:
            stack_list.append(tree.left)
        if tree.right:
            stack_list.append(tree.right)
        post_list.append(tree.val)
    post_list.reverse()
    return post_list


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
    print(preorder(tree))
    print(inorder(tree))
    print(postorder(tree))