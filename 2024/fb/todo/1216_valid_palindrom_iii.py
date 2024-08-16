'''
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true

'''
from typing import List
import math
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [[math.inf] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 0
            for j in range(i-1, -1, -1):
                if i - j == 1:
                    if s[j] == s[i]:
                        dp[j][i] = 0
                        continue
                dp[j][i] = min(dp[j+1][i], dp[j][i-1]) + 1
                if s[i] == s[j]:
                    dp[j][i] = min(dp[j][i], dp[j+1][i-1])

        if dp[0][len(s)-1] <= k:
            return True
        return False


sol = Solution()
print(sol.isValidPalindrome("abcdeca", 2))
print(sol.isValidPalindrome("abbababa", 1))

