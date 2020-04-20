'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        self.dfsSearch(candidates, target, [], res)
        return res

    def dfsSearch(self, nums, target, cur_res, res):
        if target == 0:
            res.append(cur_res)
            return
        if len(nums) == 0:
            return

        n = nums[0]
        i = 0
        while i < len(nums) and nums[i] == n:
            i += 1

        for j in xrange(i+1):
            if j * n > target:
                break
            self.dfsSearch(nums[i:], target-j*n, cur_res + [n]*j, res)

if __name__ == '__main__':
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print sol.combinationSum2(candidates, target)


        
