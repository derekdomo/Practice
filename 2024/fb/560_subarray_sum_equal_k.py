class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = {}
        count = 0
        cur_sum = 0
        for n in nums:
            cur_sum += n
            if cur_sum - k in pre_sum:
                count += pre_sum[cur_sum-k]
            pre_sum[cur_sum] = pre_sum.get(cur_sum, 0) + 1

        return count
