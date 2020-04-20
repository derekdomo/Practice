'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dic = {}
        for word in wordDict:
            dic[word] = True

        memo = [False] * len(s)

        for i in xrange(len(s)):
            if s[:i+1] in dic:
                memo[i] = True
                continue
            for j in xrange(1, i):
                if memo[j-1] and s[j:i+1] in dic:
                    memo[i] = True
                    break
        return memo[-1]

sol = Solution()
print sol.wordBreak('catssanddog', ["cats", "dog", "sand", "and", "cat"])
