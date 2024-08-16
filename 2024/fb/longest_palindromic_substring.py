class Solution:
    def longestPalindrom(self, s):
        dp = [[False] * len(s) for _ in range(len(s))]
        max_len = 1
        max_str = s[0]

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (dp[j+1][i-1] or i-j==1):
                    dp[j][i] = True
                    if i - j + 1 > max_len:
                        max_len = i-j+1)
                        max_str = s[j:i+1]
            
        return max_len

