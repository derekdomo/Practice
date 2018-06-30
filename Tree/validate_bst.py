from tree_node import TreeNode


def validate_bst(root):
    flag, val_range = dfs_validate(root)
    return flag


def dfs_validate(root):
    if root is None:
        return True, []
    left_flag, left_range = dfs_validate(root.left)
    if not left_flag:
        return False, []
    right_flag, right_range = dfs_validate(root.right)
    if not right_flag:
        return False, []
    flag, merged = merge_interval(left_range, right_range, root.val)
    if flag:
        return True, merged
    return False, []


def merge_interval(left, right, val):
    if left is [] and right is []:
        return True, [val, val]
    if left is []:
        if val < right[0]:
            return True, [val, right[1]]
        return False, []
    if right is []:
        if val > left[1]:
            return True, [left[0], val]
        return False, []

    if left[1] <= val <= right[0]:
        return True, [left[0], right[1]]
    return False, []


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    print validate_bst(root)