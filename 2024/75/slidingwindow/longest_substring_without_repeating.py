"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def solve(self, s):
        # maintain a dictionary to track all the letters in the window
        # if find a char's occurence is larger than 1, move left
        # otherwise move right side of the window
        left = 0
        right= 1
        occur = {s[0]: 1}
        max_len = 1
        while left < len(s):
            # move right side to see more char
            while right < len(s):
                if s[right] not in occur:
                    occur[s[right]] = 1
                    right += 1
                else:
                    break
            # we should have seen the longest substring with left
            max_len = max(max_len, right-left)
            if right == len(s):
                break
            # move left until we see another s[right] and move left past it
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    break
                else:
                    del occur[s[left]]
                    left += 1
            if left == right:
               right = left + 1

        return max_len

sol = Solution()
print(sol.solve("pwwkew"))


