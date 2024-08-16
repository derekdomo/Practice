"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

"""
from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        inf = 2**31 - 1
        def bfsFromRoom(rooms, x, y, visited):
            from collections import deque
            queue = deque([(x, y, 0)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while len(queue) > 0:
                i, j, step = queue.popleft() 
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                for d_i, d_j in directions:
                    n_i, n_j = i + d_i, j + d_j
                    if n_i < 0 or n_j < 0 or n_i >= len(rooms) or n_j >= len(rooms[0]):
                        continue
                    # 1.gate, update and exit
                    if rooms[n_i][n_j] == 0:
                        print(x, y)
                        rooms[x][y] = step + 1
                        return
                    # empty room, append to queue
                    if rooms[n_i][n_j] != -1 and (n_i, n_j) not in visited:
                        queue.append((n_i, n_j, step+1))
            def bfsFromGate(rooms, x, y, visited):
            from collections import deque
            queue = deque([(x, y, 0)])
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            while len(queue) > 0:
                i, j, step = queue.popleft() 
                if (i, j) in visited:
                    continue
                rooms[i][j] = step
                visited.add((i, j))
                for d_i, d_j in directions:
                    n_i, n_j = i + d_i, j + d_j
                    if n_i < 0 or n_j < 0 or n_i >= len(rooms) or n_j >= len(rooms[0]):
                        continue
                    # 1.gate, continue
                    if rooms[n_i][n_j] == 0:
                        continue
                    # 2.empty room, update
                    if rooms[n_i][n_j] == inf  and (n_i, n_j) not in visited:
                        queue.append((n_i, n_j, step+1))
        count_gate = 0
        count_room = 0
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == inf:
                    count_room += 1 
                elif rooms[i][j] == 0:
                    count_gate += 1
        if count_gate > count_room:
            for i in range(len(rooms)):
                for j in range(len(rooms[i])):
                    if rooms[i][j] == inf:
                        bfsFromRoom(rooms, i, j)
                    elif rooms[i][j] == 0:
                        bfsFromGate(rooms, i, j)



sol = Solution()
mat = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
sol.wallsAndGates(mat)
print(mat)

