class Solution:
    def generate_combinations(self, arr):
        res = []
        cur_res = []
        self.dfs_helper(arr, cur_res, res)
        return res

    def dfs_helper(self, arr, cur_res, res):
        if len(arr) == 0:
            res.append(cur_res)
            return
        cur_ele = arr[0]
        self.dfs_helper(arr[1:], cur_res + [cur_ele], res)
        self.dfs_helper(arr[1:], cur_res + [], res)


if __name__ == '__main__':
    sol = Solution()
    print sol.generate_combinations([1,2,3])
