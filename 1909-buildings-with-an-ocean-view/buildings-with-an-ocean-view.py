class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        maxHeight = -1
        res = collections.deque([])
        n = len(heights)

        if not heights:
            return []
        
        for i in reversed(range(n)):
            currHeight = heights[i]
            if currHeight > maxHeight:
                res.appendleft(i)
                maxHeight = currHeight
        return res
        