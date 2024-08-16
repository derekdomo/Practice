class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, lambda x: x[0])
        preInterval = interval[0]
        for interval in intervals[1:]:
            if preInterval[1] < interval[0]:
                return False
        
        return True
