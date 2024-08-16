class Solution:
    def diameter_of_tree(self, root):
        def backtrack(root) -> Tuple[int, int]:
            if root == None:
                return 0, 0
            left, max_left = backtrack(root.left)
            right, max_right = backtrack(root.right)
            max_len = max(left+right+1, max_left, max_right)
            return max(left, right) + 1, max_len
        
        _, max_len = backtrack(root)
        return max_len - 1

