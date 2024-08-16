def wordSearch(board, i, j,  word):
    if len(word) == 0:
        return True

    if visited[i][j]:
        return False
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for direction_x, direction_y in directions:
        visited[i][j] = True
        if board[i][j] == word:
            wordSearch(board, i+direction_x, j+direction_y, word)


    

    def dfs(self, i, j, visited, word, board, m, n):
        if len(word) == 0:
            return True
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        if visited[i][j]:
            return False
        directions = [(-1,0), (1,0), (0, -1), (0, 1)]
        if board[i][j] == word[0]:
            visited[i][j] = True
            for a, b in directions:
                if self.dfs(i+a, j+b, visited, word[1:], board, m, n):
                    return True
            visited[i][j] = False
        return False