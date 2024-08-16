class Solution:
    def minMeetingRooms(self, intervals):
        intervals = sorted(intervals, lambda x: x[0])
        min_room = 1
        meeting_to_end = []
        for meeting in intervals:
            if len(meeting_to_end) > 0 and meeting[0] > meeting_to_end[0][1]:
                heapq.heappop(meeting_to_end)
                heapq.heappush(meeting_to_end, meeting[1])
            min_room = min(min_root, len(meeting_to_end))


        return min_room



