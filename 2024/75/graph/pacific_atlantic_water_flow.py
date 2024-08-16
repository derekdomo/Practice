class Solution:
    def pacificAtlantic(self, heights):
        p_visited = {}
        a_visited = {}
        ret = []

        for i in range(len(heights)):
            self.dfsFromOcean(heights, i, 0, p_visited)
            self.dfsFromOcean(heights, i, len(heights[-])-1, a_visited)

        for i in range(len(heights[0])):
            self.dfsFromOcean(heights, 0, i, p_visited)
            self.dfsFromOcean(heights, len(heights)-1, i, a_visited)
            
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in p_visited  and (i, j) in a_visited:
                    ret.append((i,j))

        return ret


    
    def dfsFromOcean(self, heights, i, j, visited):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        if (i, j) in visited:
            return

        visited[(i, j)] = True

        for direction in directions:
            n_i, n_j = i + direction[0], j+direction[1]
            if n_i<0 or n_j<0 or n_i >= len(heights) or n_j >= len(heights[0]):
                continue
            if heights[n_i][n_j] < heights[i][j]:
                continue
            self.dfsFromOcean(heights, n_i, n_j, visited)

