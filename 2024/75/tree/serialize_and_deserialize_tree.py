class Solution:
    def seralize(self, root):
        ret = []
        #pre order traversal
        def dfs(root, ret):
            if root == None:
                ret.append('#')
                return
            ret.append(root.val)
            dfs(root.left, ret)
            dfs(root.right, ret)

        dfs(root, ret)
        return ','.join(ret)

    def deserialize(self, s):
        val = s.split(',')

        def dfs(val):
            if val[0] == '#':
                return None, val[1:]
            root = TreeNode(val[0])
            root.left, val = dfs(val[1:])
            root.right, val = dfs(val)

            return root, val
        
        root, _ = dfs(val)
        return root


