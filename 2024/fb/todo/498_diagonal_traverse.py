'''
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.


Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]


Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''
from typing import List
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        ret = []
        up = True
        i, j = 0, 0
        while True:
            if i == len(matrix)-1 and j == len(matrix[0]) - 1:
                ret.append(matrix[i][j])
                break
            ret.append(matrix[i][j])
            if up:
                i -= 1
                j += 1
                if i < 0 and j >= len(matrix[0]):
                    i = 1
                    j = len(matrix[0]) - 1
                    up = False
                elif i < 0:
                    i = 0
                    up = False
                elif j >= len(matrix[0]):
                    up = False
                    i += 2
                    j = len(matrix[0]) - 1
            else:
                i += 1
                j -= 1
                if i >= len(matrix) and j < 0:
                    i = len(matrix) - 1
                    j = 1
                    up = True
                elif i >= len(matrix):
                    i = len(matrix) - 1
                    j += 2
                    up = True
                elif j < 0:
                    j = 0
                    up = True

        return ret


sol = Solution()
print(sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.findDiagonalOrder([[1,2,3],[4,5,6]]))
                
