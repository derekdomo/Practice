class Solution:
    def treeToDoublyList(self, root):
        if root == None:
            return None
        prevNode = Node(1)
        def dfs(root, prevNode):
            if root.left == None and root.right == None:
                prevNode.right = root
                root.left = prevNode
                return root
            if root.left != None:
                prevNode = dfs(root.left, prevNode)
            prevNode.right = root
            root.left = prevNode
            prevNode = root
            if root.right != None:
                prevNode = dfs(root.right, prevNode)

            return prevNode

        lastNode = dfs(root, prevNode)
        lastNode.left = prevNode.right
        prevNode.right.left = lastNode

        return prevNode.right
