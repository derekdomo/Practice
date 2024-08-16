class Solution:
    def rob(self, nums):

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        # rob the first hosue
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])


        # do not rob the first house
        dpp = [0] * len(nums)
        dpp[0] = 0
        dpp[1] = nums[1]
        for i in range (2, len(nums)):
            dpp[i] = max(dpp[i-2]+nums[i], dpp[i-1])

        return max(dp[-2], dpp[-1])


