class Solution:
    def insert(self, intervals, newInterval):
        left,right = newInterval
        n_intervals = []
        for i, interval in enumerate(intervals):
            if newInterval[0] > interval[1]:
                n_intervals.append(interval)
                continue
            if left < interval[0]:
                n_intervals.append([left, right])
                return n_intervals + intervals[i:]
            else:
                left = min(left, interval[0])
                right = max(right, interval[1])

        return n_intervals

