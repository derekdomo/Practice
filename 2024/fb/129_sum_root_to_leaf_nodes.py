class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(self, root, pre_sum, cur_sum):
            if root == None:
                cur_sum[0] += pre_sum
                return
            pre_sum = pre_sum * 10 + root.val
            dfs(root.left, pre_sum, cur_sum)
            dfs(root.right, pre_sum, cur_sum)

        if root == None:
            return 0 

        cur_sum = [0]
        dfs(root, 0, cur_sum)
        return cur_sum[0]
