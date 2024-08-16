class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        def checkPalindrom(s):
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrom(s[left+1: right+1]) or checkPlaindrom(s[left: right])
        return True


