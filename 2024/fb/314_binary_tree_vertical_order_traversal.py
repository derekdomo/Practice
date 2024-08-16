class Solution:
    def verticalOrder(self, root):
        from collections import defaultdict
        order_dict = defaultdict(lambda _: defaultdict(list))
        def dfs(root, column, row, dict):
            if row not in dict[column]:
                order_dict[column][row] = [root.val]
            else:
                order_dict[column][row].append(root.val)
            if root.left != None:
                dfs(root.left, order-1, dict)
            if root.right != None:
                dfs(root.right, order+1, dict)

        dfs(root, 0, 0,  order_dict)
        keys = sorted(order_dict.keys())
        ret = []
        for k in keys:
            rows = order_dict[k]
            row_keys = sorted(rows.keys())
            cur = []
            for r_k in row_keys:
                cur += rows[r_k]
            ret.append(cur)
        return ret

