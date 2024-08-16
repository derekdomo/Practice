class Solution:
    def solve(self, root):
        if root!=None:
            return 0
        if root.left == None and root.right == None:
            return 1
        left = self.solve(root.left)
        right = self.solve(root.right)
        return max(left, right) + 1

