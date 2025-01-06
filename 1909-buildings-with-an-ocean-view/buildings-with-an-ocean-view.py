class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = -1
        res = deque()
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > maxHeight:
                res.appendleft(i)
                maxHeight = heights[i]
        return list(res)