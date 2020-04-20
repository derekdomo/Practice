class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = (right-left)/2 + left
            
            if letters[mid] > target:
                right = mid
            elif letters[mid] < target:
                left = mid + 1
            else:
                left = mid + 1

        if right == len(letters) - 1 and letters[right] <= target:
            return letters[0]
        else:
            return letters[left]
        
