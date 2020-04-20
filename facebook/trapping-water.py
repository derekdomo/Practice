'''
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        left = 0
        right = len(height) - 1
        water = 0
        while left < right:
            if height[left] < height[right]:
                min_bar = height[left]
                left += 1
                while left < right and height[left] <=  min_bar:
                    water += min_bar - height[left]
                    left += 1
            else: 
                min_bar = height[right]
                right -= 1
                while left < right and height[right] <= min_bar:
                    water += min_bar - height[right]
                    right -= 1
        return water

sol = Solution()
print sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
