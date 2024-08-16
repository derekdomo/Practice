"""
Problem Statement
=================
Given two sequences A = [A1, A2, A3,..., An] and B = [B1, B2, B3,..., Bm], find the length of the longest common
subsequence.

Input
=================
two lists of characters

"""

class Solution:

    def solve(self, arr_a, arr_b):
        memo_matrix = [[0 for _ in xrange(len(arr_b)+1)] for _ in xrange(len(arr_a)+1)]
        # construct memo matrix
        for i in xrange(1, len(arr_a)+1):
            for j in xrange(1, len(arr_b)+1):
                memo_matrix[i][j] = max(memo_matrix[i-1][j], memo_matrix[i][j - 1])
                if arr_a[i-1] == arr_b[j-1]:
                    memo_matrix[i][j] = max(memo_matrix[i-1][j-1] + 1, memo_matrix[i][j])

        # backtrack to rebuild the subsequence
        sub_seq = []
        i = len(arr_a)
        j = len(arr_b)
        while i > 0 and j > 0:
            if memo_matrix[i][j] == memo_matrix[i-1][j]:
                i = i-1
            elif memo_matrix[i][j] == memo_matrix[i][j-1]:
                j = j-1
            else:
                sub_seq = [arr_a[i-1]] + sub_seq
                i = i-1
                j = j-1
        return sub_seq

    def test(self):
        sequence2 = "BACDGHLQR"
        sequence1 = "AEDPHR"
        print self.solve(sequence1, sequence2)


if __name__ == '__main__':
    s = Solution()
    s.test()

