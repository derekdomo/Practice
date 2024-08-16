class Solution:
    def longestPalindrom(self, s):
        dp = [[False]* len(s) for _ in range(len(s))]
        max_len = 
        max_str = s[0]

        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and dp[j+1][i-1]:
                    dp[j][i] = True
                    if i-j+1 > max_len:
                        max_len = i-j+1
                        max_str = s[j:i+1]

        return max_str


    def longestPalindrom(self, s):
        def checkPalindrom(self, s, left, right):
            while s[left] == s[right] and left > 0 and right < len(s):
                right += 1

            return s[left+1:right-1]
        max_str = s[0]
        max_len = 1
        
        for i in range(len(s)):
            if i > 0:
                max_str = checkPalindrom(s, i-1, i)
                if max_len < len(max_str):
                    max_len = len(max_str)
                    max_str = max_str
            max_str = checkPalindrom(s, i, i)
            if max_len < len(max_str):
                max_len = len(max_str)
                max_str = max_str

        return max_str
                


