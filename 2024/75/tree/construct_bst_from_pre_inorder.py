class Solution:
    def constructTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        # preorder[0] is the root
        rootNode = TreeNode(preorder[0])
        # inorder[k]
        k = None
        for i, n in enumerate(inorder):
            if n == rootNode.val:
                k = i
                break
        # 0:k is the left side
        # k+1: is the right side
        # 1:k

        root.left = self.constructTree(preorder[1:k+1], inorder[0:k])
        root.right = self.constructTree(preorder[k+1:], inorder[k+1:])
        return root
