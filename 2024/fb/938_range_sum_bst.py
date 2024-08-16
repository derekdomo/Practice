class Solution:
    def rangeSumBST(self, root, low, high):
        sum = [0]
        def dfs(self, root, low, high, sum):
            if root == None:
                return
            if root.val >= low and root.val <= high:
                sum[0] += root.val
            dfs(root.left, low, high, sum)
            dfs(root.right, low, high, sum)

        dfs(root, low, high, sum)
        return sum[0]
