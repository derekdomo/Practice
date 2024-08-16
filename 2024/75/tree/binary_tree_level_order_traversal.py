class Solution:
    def leverOrderTraversal(self, root):
        q = [root, None]
        ret = []
        cur_list = []

        while len(q) > 0:
            n = q.popleft()
            if n == None:
                ret.append(cur_list)
                cur_list = []
                if len(q) == 0:
                    break
                q.append(None)
                continue
            cur_list.append(n.value)
            if cur.left != None:
                q.append(n.left)
            if cur.right != None:
                q.append(n.right)
    
        return ret

