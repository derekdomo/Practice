class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_area = min(height[left], height[right]) * (right-left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            max_area = max(min(height[left], height[right])*(right-left), max_area)

        return max_area


sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
