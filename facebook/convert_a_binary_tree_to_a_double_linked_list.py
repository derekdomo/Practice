class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        left, right = self.recursivelyLink(root)
        left.left = right
        right.right = left

    def recursivelyLink(self, root):
        n_left, n_right = root, root
        if root.left != None:
            n_left, right = self.recursivelyLink(root.left)
            right.right = root
            root.left = right
        if root.right != None:
            left, n_right = self.recursivelyLink(root.right)
            left.left = root
            root.right = left
        return n_left, n_right

if __name__ == '__main__':
    root = TreeNode(1, None, None)
    left = TreeNode(2, None, None)
    right = TreeNode(3, None, None)
    root.left = left
    root.right = right
    sol = Solution()
    sol.treeToDoublyList(root)
    cur = root
    print cur.val
    cur = cur.right
    while cur!=root:
        print cur.val
        cur = cur.right
