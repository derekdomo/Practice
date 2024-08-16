'''
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.


'''

class Solution:
    def sameTree(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
