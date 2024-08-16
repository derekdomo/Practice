class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s))
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue
            for j in range(i):
                if s[j:i+1] in wordDict and dp[j]:
                    dp[i] = True

        return dp[-1]
