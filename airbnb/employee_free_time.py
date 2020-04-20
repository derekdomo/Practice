'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.


Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]


(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined.)

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.
'''

class Solution:
    def employeeFreeTime(self, schedule):
        # merge intervals use heap
        cur_interval = None
        intervals = []
        import heapq
        heap = []
        for i, employee in enumerate(schedule):
            start, end = employee[0]
            heapq.heappush(heap, (start, end, i, 0))
        while len(heap) > 0:
            cur_start, cur_end, ind, i = heapq.heappop(heap)
            if cur_interval == None:
                cur_interval = (cur_start, cur_end)
            else:
                if cur_interval[1] < cur_start:
                    intervals.append(cur_interval)
                    cur_interval = (cur_start, cur_end)
                else:
                    cur_interval = (min(cur_start, cur_interval[0]), max(cur_end, cur_interval[1]))
            if i < len(schedule[ind])-1:
                n_start, n_end = schedule[ind][i+1]
                heapq.heappush(heap, (n_start, n_end, ind, i+1))

        if cur_interval is not None:
            intervals.append(cur_interval)

        free_time = []
        cur_interval = intervals[0]
        for interval in intervals[1:]:
            if cur_interval[1] < interval[0]:
                free_time.append((cur_interval[1], interval[0]))
            cur_interval = interval

        return free_time

if __name__ == '__main__':
    sol = Solution()
    print sol.employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]])

