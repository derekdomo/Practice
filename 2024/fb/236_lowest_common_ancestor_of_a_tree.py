class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if root == None:
                return None, False, False
            p_found = False
            q_found = False
            if root == p:
                p_found = True
            if root == q:
                q_found = True

            ancestor, p_left, q_left = dfs(root.left, p, q)
            if ancestor:
                return ancestor

            ancestor, p_right, q_right = dfs(root.right, p, q)
            if ancestor:
                return ancestor

            p_found = p_found or p_left or p_right
            q_found = q_found or q_left or q_right
            if p_found and q_found:
                return root, p_found, q_found
            return None, p_found, q_found
        
        ancestor, _, _ = dfs(root, p, q)
        return ancestor
