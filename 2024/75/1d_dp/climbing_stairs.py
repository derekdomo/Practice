class Solution:
    def climbStairs(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[-1]
