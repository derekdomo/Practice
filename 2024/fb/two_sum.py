class Solution:
    def twoSum(self, arr, target):
        expect_dict = {}
        ret = []
        for i, n in enumerate(arr):
            if target - n in expect_dict:
                ret.append([i, expect_dict[target-n]])
            expect_dict[target-n] = i

        return ret
            
