"""
Problem Statement
=================
0/1 Knapsack Problem - Given items of certain weights/values and maximum allowed weight how to pick items to pick items
from this set to maximize sum of value of items such that sum of weights is less than or equal to maximum allowed
weight.

Input
=================
two lists: weights and values;
one target weight


"""

class Solution:

    def solve_knapsack_01(self, weights, values, target_weight):
        num_articles = len(weights)
        memo_matrix = [[0 for i in xrange(target_weight+1)] for j in xrange(num_articles+1)]

        for i in xrange(1, num_articles+1):
            for j in xrange(1, target_weight+1):
                if weights[i-1] > j:
                    memo_matrix[i][j] = memo_matrix[i][j-1]
                else:
                    memo_matrix[i][j] = max(memo_matrix[i-1][j-weights[i-1]] + values[i-1], memo_matrix[i-1][j])
        return memo_matrix[num_articles][target_weight]

    def test(self):
        total_weight = 7
        weights = [1, 3, 4, 5]
        values = [1, 4, 5, 7]
        expected = 9

        assert expected == self.solve_knapsack_01(weights, values, total_weight)



if __name__ == '__main__':
    s = Solution()
    s.test()


