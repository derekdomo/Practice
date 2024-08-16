'''
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of nums is included in any of the ranges, and each missing number is covered by one of the ranges.

 

 

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]
Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]
Example 2:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
 
'''
from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        pre = lower - 1
        ret = []
        for n in nums:
            if n == pre + 1:
                pre = n
                continue
            else:
                ret.append([pre+1, n-1])
                pre = n

        if pre + 1 < upper:
            ret.append([pre+1, upper])

        return ret

sol = Solution()
print(sol.findMissingRanges([0,1,3,50,75], 0, 99))
print(sol.findMissingRanges([-1], -1, -1))
        
