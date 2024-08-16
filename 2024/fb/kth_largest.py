'''
215. Kth Largest Element in an Array
Medium
Topics
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
'''
class Solution:
    def kthLargest(self, nums, k):
        import heapq
        heap = []
        for n in nums:
            heapq.heappush(heap, n)

        return heap[0]

    def kthLargest(self, nums, k):
        def quickSelect(nums, k):
            import random
            pivot = random.choice(nums)
            left, mid, right = [],[],[]
            for num in nums:
                if num<nums[pivot]:
                    left.append(num)
                elif num> nums[pivot]:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quickSelect(left, k)

            if len(left) + len(mid) > k:
                return quickSelect(right, k - len(left)-len(mid))

            return pivot

        return quickSelect(nums, k)


sol = Solution()
print(sol.kthLargest([3,2,1,5,6,4], 2))


