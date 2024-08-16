class Solution:
    def countSubStrings(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        dp = [[False] * len(s) for _ in range(len(s))]

        count = 0
        for i in range(len(s)):
            dp[i][i] = True
            count += 1
            for j in range(i):
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = True
                    count += 1


        return count
