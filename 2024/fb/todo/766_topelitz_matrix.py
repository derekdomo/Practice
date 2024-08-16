'''
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.


Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.


Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
'''
from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        start = []
        for i in range(len(matrix)):
            start.append((i, 0))
        for i in range(len(matrix[0])):
            start.append((0, i))
        
        for i, j in start:
            pre = matrix[i][j]
            while i< len(matrix) and j < len(matrix[0]):
                if pre != matrix[i][j]:
                    return False
                pre = matrix[i][j]
                i += 1
                j += 1
        
        return True

sol = Solution()
print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
print(sol.isToeplitzMatrix([[1,2],[2,2]]))
