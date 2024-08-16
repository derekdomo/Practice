'''
Given a 2-D grid of characters board and a string word, return true if the word 
is present in the grid, otherwise return false.

For the word to be present it must be possible to form it with a path in the 
board with horizontally or vertically neighboring cells. 
The same cell may not be used more than once in a word.

'''
class Solution:
    def exist(self, board, word):
        def dfs(self, board, i, j, visited, word):
            if len(word) == 0:
                return True
            if word[0] != boad[i][j]:
                return False
            directions = [(0,1), (1, 0), (-1, 0), (0, -1)]
            visited.add((i, j))
            for direction in directions:
                n_i = i + direction[0]
                n_j = j + direction[1]
                if n_i<0 or n_j<0 or n_i >= len(board) or n_j>=len(board[0]):
                    continue
                if (n_i, n_j) in visited:
                    continue
                if dfs(board, n_i, n_j, visited, word[1:]):
                    return True
            visited.remove((i, j))
            
            return False
        

        for i in range(len(board)):
            for j in range(len(board[0]):
                if dfs(board, i, j, set(), word):
                    return True
        
        return False
