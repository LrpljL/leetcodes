# coding = utf-8
"""
递归+迭代
"""
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def helper(node, level, levels):
    if not node:
        return levels
    # start the current level
    if len(levels) == level:
        levels.append([])

    # append the current node value
    levels[level].append(node.val)

    # process child nodes for the next level
    if node.left:
        helper(node.left, level + 1, levels)
    if node.right:
        helper(node.right, level + 1, levels)


# 使用队列来存储每一层的节点
def levelorder(tree, levels):
    """

    :param tree:
    :param levels:
    :return:
    """
    queue = deque([tree])
    level = 0
    while queue:
        level_length = len(queue)
        levels.append([])
        for i in range(level_length):
            node = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level += 1
    return levels


if __name__ == "__main__":
    """BFS"""
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.right.left = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    # dict1 = {}  # 存储每个节点与根节点的距离
    levels = []
    helper(tree, 0, levels)
    print(levels)
    # print(levelorder(tree, levels))
