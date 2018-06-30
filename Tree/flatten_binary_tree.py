from tree_node import TreeNode

# flatten a tree as pre order

def flatten_binary_tree(root):
    if root is None:
        return None
    flatten_helper(root)

def flatten_helper(root):
    left_child = root.left
    right_child = root.right
    last_node = root
    if left_child is not None:
        last_node = flatten_helper(left_child)
        last_node.right = right_child
        root.right = left_child
        root.left = None
    if right_child is not None:
        last_node = flatten_helper(right_child)
    return last_node


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    flatten_binary_tree(root)
    while root is not None:
        print root.val
        root = root.right