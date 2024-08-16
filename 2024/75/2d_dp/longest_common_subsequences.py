class Solution:
    def longestCommonSubSequence(self, text1, text2):
        dp = [[0] * len(text1) for _ in range(len(text2))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                if text1[i] == text2[j]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]


