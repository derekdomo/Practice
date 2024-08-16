'''
Given a binary search tree (BST) where all node values are unique, and two nodes
from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor between two nodes p and q is the lowest node in a 
tree T such that both p and q as descendants. The ancestor is allowed to be a 
descendant of itself.
'''

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None or p == None or q == None:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        small = None
        large = None
        if p.val > q.val:
            small = q
            large = p
        else:
            small = p
            large = q

        if root.val > small.val and root.val < large.val:
            return root
        elif root.val > small.val and root.val > large.val:
            return self.lowestCommonAncestor(root.left, small, large)
        elif root.val < small.val and root.val < large.val:
            return self.lowestCommonAncestor(root.right, small, large)
        
        return None


