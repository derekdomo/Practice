'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and 
become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

'''

class Solution:
    def solve(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left < right:
            mid = left + (right-left)//2

            if arr[mid] == target:
                return mid
            elif arr[left]<target and target< arr[mid]:
                # rorate on the right
                right = mid + 1
            elif arr[left] < arr[mid] and (target < arr[left] or target > arr[mid]):
                # rorate on the right side
                left = mid + 1
            else:
                # rotate on the left side
                if target  > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        if target == arr[left]:
            return left
        if target == arr[right]:
            return right
        return -1


sol = Solution()
print(sol.solve([4,5,6,7,0,1,2], 3))
print(sol.solve([1], 0))


