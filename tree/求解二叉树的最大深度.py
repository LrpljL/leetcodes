# coding = utf-8
"""
二叉树的深度为根节点到最远叶子节点最长路径上的节点数
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# left_height, right_height = 0, 0


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    else:
        left_height = maxDepth(root.left)
        right_height = maxDepth(root.right)
        return max(left_height, right_height) + 1


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    print(maxDepth(tree))