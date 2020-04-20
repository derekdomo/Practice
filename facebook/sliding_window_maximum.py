class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = []
        res = []
        for i, n in enumerate(nums):
            self.pop(queue, i-k)
            queue = self.push(queue, k, (n, i))
            if i < k-1:
                continue
            res.append(queue[-1][0])
        return res

    def pop(self, queue, k):
        if k < 0:
            return
        while len(queue) > 0:
            if queue[-1][1] < k:
                queue.pop()
            else:
                break

    def push(self, queue, k, n_ele):
        for i, ele in enumerate(queue):
            if ele[0] > n_ele[0]:
                return [n_ele] + queue[i:]
        return [n_ele]

sol = Solution()
print sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
        

            


