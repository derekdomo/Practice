class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None

        low = None
        high = None
        if p.val > q.val:
            low = q
            high = p
        else:
            low = p
            high = q

        def dfs(root, low, high):
            if root.val == low.val or root.val == high.val:
                return root
            if root.val > low.val and root.val < high.val:
                return root
            elif root.val > low.val and root.val > high.val:
                return dfs(root.left, low, right)
            else:
                return dfs(root.right, low, right)

        return dfs(root, low, high)
