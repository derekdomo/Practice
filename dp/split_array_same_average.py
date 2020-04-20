class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        total_sum = sum(A)
        target_average = total_sum * 1.0 / len(A)
        A.sort()

