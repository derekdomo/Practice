from typing import List
class Solution:
    def solve(self, arr: List[int], target: int) -> List[int]:
        s_arr = sorted(arr)
        ret = []
        for i, n in enumerate(s_arr):
            if i > 0 and s_arr[i] == s_arr[i-1]:
                continue
            res = self.twoSum(s_arr[i+1:], target-n)
            if len(res) != 0:
                ret = ret + [[n]+s for s in res]

        return ret
    
    def twoSum(self, arr, target):
        left = 0
        right = len(arr)-1
        ret = []
        while left < right:
            if arr[left] + arr[right] > target:
                right -= 1
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                ret.append([arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1

                while left < right and arr[right] == arr[right-1]:
                    right -= 1

        return ret


sol = Solution()
s = sol.solve([1,2,2,2,3,4,5,6], 10)
print(s)
