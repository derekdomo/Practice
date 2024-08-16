class Solution:
    def findKthLargest(self, nums, k):
        def quickSelect(nums, k):
            less = []
            equal = []
            more = []
            pivot = nums[0]
            for n in nums:
                if n == pivot:
                    equal.append(n)
                elif n > pivot:
                    more.append(n)
                else:
                    less.append(n)

            if len(more) >= k:
                return quickSelect(more, l)
            elif len(more) + len(equal) >= k:
                return pivot
            else:
                return quickSelect(less, k - len(more) - len(equal))

        return quickSelect(nums, k)
