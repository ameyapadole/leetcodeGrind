class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 
        intervals.sort(key = lambda x : x[0])
        rooms = [intervals[0][1]]

        for start, end in intervals[1:]:
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
        return len(rooms)
        