class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.cur = 0

    def construct_tree(self, inorder, preorder, start, end):
        if start > end:
            return None
        root = TreeNode(preorder[self.cur])
        index = -1
        # find split point for inorder sequence
        for i in xrange(start, end+1):
            if preorder[self.cur] == inorder[i]:
                index = i
                break
        self.cur += 1
        root.left = self.construct_tree(inorder, preorder, start, index-1)
        root.right = self.construct_tree(inorder[index+1:], preorder, index+1, end)
        return root


if __name__ == "__main__":
    s = Solution()
    s.construct_tree([1, 2], [2, 1], 0, 1)