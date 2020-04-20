"""
Definition of Interval.
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        timestamp = {}
        for interval in intervals:
            timestamp[interval[0]] = timestamp.get(interval[0], 0) + 1
            timestamp[interval[1]] = timestamp.get(interval[1], 0) - 1

        timestamps = sorted(timestamp.keys())
        max_room = 0
        cur_room = 0
        for t in timestamps:
            cur_room += timestamp[t]
            max_room = max(max_room, cur_room)

        return max_room

sol = Solution()
print sol.minMeetingRooms([(0,30),(5,10),(15,20)])
