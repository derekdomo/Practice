class Solution:
    def isPalindrom(self, x):
        s = str(x)
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
