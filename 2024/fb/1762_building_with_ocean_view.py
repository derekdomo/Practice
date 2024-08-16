from typing import List
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = heights[-1]-1
        oc_view = []
        for i, n, in enumerate(heights[::-1]):
            if n > max_height:
                oc_view.append(len(heights) - i - 1)
                max_height = n
        
        return oc_view[::-1]

sol = Solution()
print(sol.findBuildings([4,2,3,1]))
print(sol.findBuildings([4,3,2,1]))
print(sol.findBuildings([1,3,2,4]))

