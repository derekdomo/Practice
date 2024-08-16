class Solution:
    def numDecodeWays(self, s):
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        if s[0] == '0':
            return 0

        for i in range(1, len(s)):
            if s[i] == '0':
                if int(s[i-1:i+1]) > 26 and int(s[i-1:i+1])!=0:
                    dp[i+1] = dp[i-1]
                else:
                    dp[i+1] = 0
            else:
                if int(s[i-1:i+1]) <= 26 amd s[i-1] != '0':
                    dp[i+1] = dp[i-1] + dp[i]
                else:
                    dp[i+1] = dp[i]

        return dp[-1]
