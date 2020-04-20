class Solution:
    def generate_all_adjacent_combinations(self, arr):
        res = []
        cur_res = []
        self.dfs_helper(arr, 0, cur_res, res)
        return res

    def dfs_helper(self, arr, ind, cur_res, res):
        if ind == len(arr):
            res.append(cur_res)
            return
        acc = 0
        for i in xrange(ind, len(arr)):
           acc = acc*10 + arr[i]
           self.dfs_helper(arr, i+1, cur_res+[acc], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.generate_all_adjacent_combinations([1,2,3])

        
