'''
Given the roots of two binary trees root and subRoot, return true if there is a
subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. The tree tree could also be considered as a subtree of itself.
'''

class Solution:
    def isSubTree(self, root, subRoot):
        def dfs(p, q):
            if p == None and q == None:
                return True
            if p == None or q == None:
                return False
            if p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            return False

        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        
        if root.val == subRoot.val:
            return dfs(root, subRoot) or self.isSubTree(root.left, subRoot) 
                or self.isSubTree(root.right, subRoot) 
        return False
