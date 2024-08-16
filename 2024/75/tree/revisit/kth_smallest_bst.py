'''
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
'''

class Solution:
    def solve(self, root, k):
        def dfs(root, k, ret):
            if k < 1:
                return k
            if root == None:
                return k
            k = dfs(root.left, k, ret)
            if k == 1:
                ret[0] = root.val
                return -1
            k = dfs(root.right, k-1, ret)
            return k
        
        ret = [None]
        self.dfs(root, k, ret)
        return ret[0]
