from tree_node import TreeNode


def validate_bst(root):
    val_left = dfs_validate(root.left)
    if val_left < root.val:
        return True
    val_right = dfs_validate(root.right)
    if val_right > root.val:
        return False
    
def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> bool:
            if root is None:
                return True
            if not dfs(root.left):
                return False
            nonlocal prev
            if prev >= root.val:
                return False
            prev = root.val
            return dfs(root.right)

        prev = -inf
        return dfs(root)




if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    print validate_bst(root)