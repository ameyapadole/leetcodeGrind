class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        intervals.sort()
        # n Log n
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True

        # Time = O(n LogN)
        # Space = O(1)
            

        