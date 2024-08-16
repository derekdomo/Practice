'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        pre = intervals[0]
        ret = []
        for interval in intervals[1:]:
            if interval[0] > pre[1]:
                ret.append(pre)
                pre = interval
            else:
                pre = [min(pre[0], interval[0]), max(pre[1], interval[1])]

        ret.append(pre)
        return ret

sol = Solution()
print(sol.merge( [[1,3],[2,6],[8,10],[15,18]]))
print(sol.merge([[1,4],[4,5]]))




