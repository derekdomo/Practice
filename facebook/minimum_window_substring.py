'''
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

sliding window
 left and right
 move right to find all the matches
 move left to find the minimum matches
'''


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq_map = {}
        for c in t:
            freq_map[c] = freq_map.get(c, 0) + 1

        cur_map = dict(freq_map)
        remaining_char = len(cur_map)
        left = -1
        min_length = len(s)
        res = ""
        right = left

        # left is exclusive
        while right < len(s)-1:
            while right < len(s)-1:
                right += 1
                c = s[right]
                if c in cur_map:
                    cur_map[c] -= 1
                    if cur_map[c] == 0:
                        remaining_char -= 1
                    if remaining_char == 0:
                        break

            if remaining_char != 0:
                break

            if right - left <= min_length:
                min_length = right - left 
                res = s[left+1:right+1]

            while left < right:
                left += 1
                c = s[left]
                if c in cur_map:
                    cur_map[c] += 1
                    if cur_map[c] == 1:
                        remaining_char += 1
                        break
                if right - left <= min_length:
                    min_length = right - left 
                    res = s[left+1:right+1]

        return res

sol = Solution()
print sol.minWindow("a", "ab")

        
