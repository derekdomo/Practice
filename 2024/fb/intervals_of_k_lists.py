from typing import List
class Solution:
    def intersection(self, lists: List[List[List[int]]]) -> List[int]:
        def _intersect(left, right):
            if left == None or right == None:
                return None
            if left[0] > right[1] or left[1] < right[0]:
                return None
            return [max(left[0], right[0]), min(left[1], right[1])]
        def _intersection(l: List[List[int]]) -> List[int]:
            if len(l) == 1:
                return l[0]
            if len(l) == 2:
                return _intersect(l[0], l[1])
            mid = len(l) // 2
            left = _intersection(l[:mid+1])
            right = _intersection(l[mid+1:])
            return _intersect(left, right)

        ret = []
        for l in lists:
            ret.append(_intersection(l))

        return _intersection(ret)

sol = Solution()
print(sol.intersection([
        #[[4,12], [2,5], [2,5], [3, 5], [2, 9]],
        [[1,10], [2,5], [2,5], [3, 5], [3, 9]]
    ]))
            


