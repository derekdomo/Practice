class Solution:
    def printPath(self, nested_list):
        def dfs(nested_list, parent, result):
            if len(nested_list) == 0:
                result.append(parent)
                return
            pre = parent
            for c in nested_list:
                if type(c) is list:
                    dfs(c, pre, result)
                else:
                    pre = parent + '->' + c
                    result.append(pre)

        pre = None
        result = []
        for char in nested_list:
            if type(char) is list:
                dfs(char, pre, result)
            else:
                pre = char
                result.append(pre)
        return result

sol = Solution()
print(sol.printPath(['A', 'B', ['C', 'D'], ['E', ['F',['G', 'H']]]]))
        

