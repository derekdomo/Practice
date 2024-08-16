class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, lambda x: x[1])

        preInterval = interval[0]
        count += 1

        for interval in intervals[1:]:
            if preInterval[1] <= interval[0]:
                preInterval = interval
                count += 1


        return len(intervals) - count

