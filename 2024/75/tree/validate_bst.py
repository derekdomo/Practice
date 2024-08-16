class Solution:
    def isValidBST(self, root):
        def dfs(node, max_val, min_val):
            if node == None:
                return True
            if node.val < max_val and node.val > min_val:
                return dfs(node.left, node.val, min_val) and dfs(node.right, max_val, node.val)
            return False

        return dfs(root.left, root.val, -math.inf) and dfs(root.right, math.inf, root.val):


