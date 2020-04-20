'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        freq_map = {}
        for c in p:
            freq_map[c] = freq_map.get(c, 0) + 1
        
        left = 0
        right = 0
        cur_map = dict(freq_map)
        res = []
        # when to move left side
        #   when right is not in freq map
        #       not in map at all
        #           move to right
        #       in map but deleted
        #           left increment to first b and recover
        # when to move right side
        while left + len(p) <= len(s):
            right = left
            while right < left + len(p) and left + len(p)<= len(s):
                print s, left, right,cur_map
                if s[right] not in freq_map:
                    left = right + 1
                    cur_map = dict(freq_map)
                    right = left
                elif s[right] in cur_map:
                    cur_map[s[right]] -= 1
                    if cur_map[s[right]] == 0:
                        del cur_map[s[right]]
                    if len(cur_map) == 0:
                        res.append(left)
                        cur_map[s[left]] = 1
                        left += 1
                    right += 1
                else:
                    # move left to first right and recover
                    while s[left] != s[right]:
                        cur_map[s[left]] = cur_map.get(s[left], 0) + 1
                        left += 1
                    left += 1
                    right += 1
                
        return res

sol = Solution()
s = "abab"
p = "ab"
print sol.findAnagrams(s, p)
