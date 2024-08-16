class Solution:
    def find_local_minimum(self, nums):
        pre = None
        ret = []
        for i, n in enumerate(nums[:-1]):
            if i == 0:
                pre = n
                continue
            if pre == n:
                continue
            if pre > n and n < nums[i+1]:
                ret.append(i)
            elif pre > n and n == nums[i+1]:
                continue
            pre = n
        return ret

sol = Solution()
nums = [3,2,2,4,5,6]
print(nums)
print(sol.find_local_minimum(nums))
        

