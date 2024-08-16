class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root):
    #in order traversal
    dfs(root.left)
    # do something and return
    root
    # do something and return
    dfs(root.right)
    # do something and return