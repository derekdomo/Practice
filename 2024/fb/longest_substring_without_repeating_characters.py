class Solution:
    def lengthOfLongestSubString(self, s):
        left = 0 
        right = 1
        if len(s) < 1:
            return len(s)
        max_len = 1

        seen_dict = {s[0]:0}
        while right < len(s):
            if s[right] not in seen_dict:
                seen_dict[s[right]] = right
                right += 1
                max_len = max(max_len, right - left)
            else:
                while s[left] in seen_dict and left < right:
                    del seen_dict[s[left]]
                    left += 1
        
        return max_len
