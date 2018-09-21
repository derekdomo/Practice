class Solution:
    def solve(self, time_intervals):
        time_intervals.sort(key = lambda x: x[1])
        maximum_overlapped_intervals = 1 
        for i in xrange(0, len(time_intervals)):
            overlapped_interval = time_intervals[i]
            current_overlapped = 1
            for j in xrange(i+1, len(time_intervals)):
                new_overlap = self.check_overlap(overlapped_interval, time_intervals[j])
                if new_overlap is None:
                    break
                else:
                    overlapped_interval = new_overlap
                    current_overlapped += 1
                    maximum_overlapped_intervals = max(maximum_overlapped_intervals, current_overlapped)
        return maximum_overlapped_intervals


    def check_overlap(self, interval_one, interval_two):
        if interval_one[1] <= interval_two[0]:
            return None 
        elif interval_one[0] >= interval_two[0]:
            return [interval_two[0], interval_one[1]]
        else:
            return [interval_one[0], interval_one[1]]

if __name__ == '__main__':
    sol = Solution()
    print sol.solve([[1,3], [2,3], [2,5], [3, 5], [3, 6]])