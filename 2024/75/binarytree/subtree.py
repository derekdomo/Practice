# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None or subRoot == None:
            return False
        if root == None and subRoot == None:
            return True
        if self.isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, r, s):
        if r == None and s == None:
            return True
        if r and s and r.val == s.val:
            return self.isSame(r.left, s.left) and self.isSame(r.right, s.right)
        return False

    def isSubtree(self, root, subRoot)    
    if root == None or subRoot == None:
        return False
    if root == None and subRoot == None:
        return True
    if root.val == subRoot.val:
        return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)
    if root != subRoot:
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        