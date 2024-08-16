class Solution:
    def numIslands(self, grid):
        def dfs_coloring(grid, i, j):
            grid[i][j] = '-1'
            directions = [(0,1), (1,0), (0,-1),(-1,0)]
            for direction in directions:
                n_i = i + direction[0]
                n_j = j + direction[1]
                if n_i < 0 or n_j<0 or n_i>=len(grid) or n_j >=len(grid[0]):
                    continue
                if grid[n_i][n_j] == '1':
                    dfs_coloring(board, n_i, n_j)
            return
        
        n_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    n_islands += 1
                    dfs_coloring(grid, i, j)

        return n_islands
