class Solution:
    def generate_combination_of_k(self, arr, k):
        cur_res = []
        res = []
        self.dfs_helper(arr, k, cur_res, res)
        return res

    def dfs_helper(self, arr, k, cur_res, res):
        if k == 0:
            res.append(cur_res)
            return
        if len(arr) == 0 or k < 0:
            return
        cur_ele = arr[0]
        self.dfs_helper(arr[1:], k-1, cur_res+[cur_ele], res)
        self.dfs_helper(arr[1:], k, cur_res+[], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.generate_combination_of_k([1,2,3,4], 2)

