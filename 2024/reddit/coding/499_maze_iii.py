from typing import List

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        # memorize wall positions
        from collections import defaultdict
        rows = defaultdict(list)
        cols = defaultdict(list)
        for i in range(len(maze)):
            rows[i].append(-1)
            for j in range(len(maze[0])):
                if maze[i][j] == 1:
                    rows[i].append(j)
                    cols[j].append(i)
            rows[i].append(len(maze[0]))
        for j in range(len(maze[0])):
            cols[j] = [-1] + cols[j]
            cols[j].append(len(maze))
        
        import heapq
        queue = []
        queue.append((0, '', ball[0], ball[1]))
        visited = set()

        while len(queue) > 0:
            distance, path, i, j = heapq.heappop(queue)
            if i == hole[0] and j == hole[1]:
                return path
            if (i, j) in visited:
                continue
            visited.add((i, j))
            # go left
            n_j = self.findFirstSmaller(rows[i], j)+1
            if i == hole[0] and hole[1]>n_j and hole[1]<j:
                heapq.heappush(queue, (distance+j-hole[1], path+'l', i, hole[1]))
            heapq.heappush(queue, (distance+j-n_j, path+'l', i, n_j))

            # go right
            n_j = self.findFirstLarger(rows[i], j)-1
            if i == hole[0] and hole[1]<n_j and hole[1]>j:
                heapq.heappush(queue, (distance+hole[1]-j, path+'r', i, hole[1]))
            heapq.heappush(queue, (distance+n_j-j, path+'r', i, n_j))

            # go up
            n_i = self.findFirstSmaller(cols[j], i)+1
            if j == hole[1] and hole[0]>n_i and hole[0]<i:
                heapq.heappush(queue, (distance+i-hole[0], path+'u', hole[0], hole[1]))
            heapq.heappush(queue, (distance+i-n_i, path+'u', n_i, j))
            
            # go down
            n_i = self.findFirstLarger(cols[j], i)-1
            if j == hole[1] and hole[0]>i and hole[0]<n_i:
                heapq.heappush(queue, (distance+hole[0]-i, path+'d', hole[0], hole[1]))
            heapq.heappush(queue, (distance+n_i-i, path+'d', n_i, j))
        
        return 'impossible'

    def findFirstSmaller(self, arr, target):
        left = 0 
        right = len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right-left)//2
            if target > arr[mid]:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return arr[result]
    
    def findFirstLarger(self, arr, target):
        left = 0 
        right = len(arr) - 1
        result = -1
        while left <= right:
            mid = left + (right-left)//2
            if target < arr[mid]:
                result = mid
                right = mid - 1
            else:
                left = mid+1
        return arr[result]


sol = Solution()
print(sol.findShortestWay([[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], [4,3], [0,1]))
