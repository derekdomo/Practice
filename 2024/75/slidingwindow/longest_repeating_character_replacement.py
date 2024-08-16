"""
You are given a string s and an integer k. You can choose any character of the 
string and change it to any other uppercase English character. You can perform 
this operation at most k times.

Return the length of the longest substring containing the same letter you can 
get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

class Solution:
    def solve(self, s, k):
        # maintain a dictionary of all the letters we have seen
        # if the most appeared char + k is the dictionary size,
        # we are hitting the limit
        # we need to move one side of the window to update

        dict = {s[0]: 1}
        left = 0
        right = 1
        most_appear_char = s[0]
        most_occur_count = 1
        max_len = 1
        
        while right < len(s):
            while right < len(s):
                if s[right] in dict:
                    dict[s[right]] += 1
                else:
                    dict[s[right]] = 1

                if dict[s[right]] > most_occur_count:
                    most_appear_char = s[right]
                    most_occur_count = dict[s[right]]
                right += 1
                
                if right - left > k + most_char_count:
                    # we are hitting the window size limit
                    break
                
                max_len = max(max_len, right-left)

            if right == len(s):
                break

            dict[s[left]] -= 1
            left += 1

            # recheck the most occur char
            most_appear_char = None
            most_occur_count = 0
            for c in dict:
                if dict[c] > count:
                    most_occur_count = dict[c]
                    most_appear_char = c

        return max_len



