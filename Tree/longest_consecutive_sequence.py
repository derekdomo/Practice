from tree_node import TreeNode


def get_longest_consecutive_sequence(root):
    optimal_res = [0]
    dfs_helper(root, optimal_res, True)
    return optimal_res[0]


def dfs_helper(root, optimal_res, inc=True):
    if root is None:
        return 0
    max_left = 0
    max_right = 0
    if root.left is not None and root.val - root.left.val == 1 and not inc:
        max_left = dfs_helper(root.left, optimal_res, not inc)
    elif root.left is not None and root.left.val - root.val == 1 and inc:
        max_left = dfs_helper(root.left, optimal_res, inc)
    else:
        dfs_helper(root.left, optimal_res, inc)
    if root.right is not None and root.val - root.right.val == 1 and not inc:
        max_right = dfs_helper(root.right, optimal_res, not inc)
    elif root.right is not None and root.right.val - root.val == 1 and inc:
        max_right = dfs_helper(root.right, optimal_res, inc)
    else:
        dfs_helper(root.right, optimal_res, inc)

    max_cur = 1 + max(max_left, max_right)
    optimal_res[0] = max(max_cur, optimal_res[0])
    return max_cur


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(3)
    root.left.right.left = TreeNode(4)
    print get_longest_consecutive_sequence(root)