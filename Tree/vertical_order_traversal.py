from tree_node import TreeNode
from collections import defaultdict


def vertical_order_traversal(root):
    offset_map = defaultdict(list)
    dfs(root, offset_map, 0)
    index_list = offset_map.keys()
    min_index = min(index_list)
    max_index = max(index_list)
    for i in xrange(min_index, max_index+1):
        l = offset_map[i]
        for n in l:
            print n.val
        print "------------"


def dfs(root, offset_map, index):
    if root is None:
        return
    dfs(root.left, offset_map, index+1)
    offset_map[index].append(root)
    dfs(root.right, offset_map, index-1)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    vertical_order_traversal(root)