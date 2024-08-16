class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root == None:
            return root
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        root.left = l
        root.right = r

        return root

