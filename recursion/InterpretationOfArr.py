class Solution:
    def interpretation_of_array(self, arr):
        res = []
        cur_res = []
        self.dfs_helper(0, arr, cur_res, res)
        return res

    def dfs_helper(self, ind, arr, cur_res, res):
        if ind == len(arr):
            res.append(cur_res)
            return
        # single number
        self.dfs_helper(ind+1, arr, cur_res+[chr(arr[ind]+96)], res)
        # two numbers
        if ind < len(arr)-1:
            num = arr[ind]*10 + arr[ind+1]
            if num <= 26:
                self.dfs_helper(ind+2, arr, cur_res+[chr(num+96)], res)

if __name__ == '__main__':
    sol = Solution()
    print sol.interpretation_of_array([1,2,3,4])
    
