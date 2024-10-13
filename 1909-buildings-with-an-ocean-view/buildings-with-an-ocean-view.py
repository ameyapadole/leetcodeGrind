class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        maxHeight = -1

        if not heights:
            return []
        
        res = collections.deque([])
        for i in range(len(heights) - 1, -1, -1):
            currHeight = heights[i]
            if currHeight > maxHeight:
                res.appendleft(i)
                maxHeight = currHeight
        return res
        