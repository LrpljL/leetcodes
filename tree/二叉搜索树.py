# coding = utf-8
"""求解二叉搜索树的个数
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# def numTrees(n):
#     if n==1 or n==0:
#         return 1
#     num = 0
#     for i in range(1, n+1, 1):
#         num += numTrees(i-1)*numTrees(n-i)
#     return num


def numTrees(n):
    list1 = [0 for i in range(n+1)]
    list1[0], list1[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            list1[i] += list1[j-1]*list1[i-j]
    return list1[n]


def generate_trees(start, end):
    if start > end:
        return [None, ]

    all_trees = []
    for i in range(start, end + 1):  # pick up a root

        left_trees = generate_trees(start, i - 1)

    # all possible right subtrees if i is choosen to be a root
        right_trees = generate_trees(i + 1, end)

    # connect left and right subtrees to the root i
        for l in left_trees:
            for r in right_trees:
                current_tree = TreeNode(i)
                current_tree.left = l
                current_tree.right = r
                all_trees.append(current_tree.val)

    return all_trees

    # return generate_trees(1, n) if n else []


if __name__ == "__main__":
    print(numTrees(4))
    # print(generate_trees(1, 10))