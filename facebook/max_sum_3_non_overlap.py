class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        memo = [[(0, None) for i in xrange(len(nums))] for j in xrange(len(nums))]
        for i in xrange(len(nums)-k):
            for j in xrange(i+k-1, len(nums)):
                total = sum(nums[j-k+1:j+1])
                if memo[i][j][0] < total:
                    memo[i][j] = (total, j-k+1)
        best = []
        best_sum = 0
        for i in xrange(k-1, len(nums)-2k):
            cur_sum = memo[0][i][0]
            for j in xrange(i+k, len(nums)-k):
                if best_sum < cur_sum + memo[i+1][j-1][0] + memo[j][len(nums)-1][0]:
                    best = [memo[0][i][1], memo[i+1][j-1][1], memo[j][len(nums)-1][1]]
        
        return best
                
        
