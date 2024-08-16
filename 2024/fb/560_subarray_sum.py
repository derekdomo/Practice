class Solution:
    def subArraySum(self, nums, k):
        total = 0
        preSum = {0: 1}
        count = 0
        for n in nums:
            total += n
            if total - k:
                count += preSum[total-k]
            preSum[total] = preSum.get(total, 0) + 1
        return count
