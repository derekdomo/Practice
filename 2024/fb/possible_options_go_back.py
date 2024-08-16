class Solution:
    def traverseBack(self, length, ind, steps):
        def dfs(length, ind, target, steps):
            if steps == 1:
                return 1
            if steps == 0 and ind == target:
                return 1
            count = 0
            for i in range(length):
                count += dfs(length, i, target, steps-1)
            return count
        
        return dfs(length, ind, ind, steps)

sol = Solution()
print(sol.traverseBack(10, 3, 3))

