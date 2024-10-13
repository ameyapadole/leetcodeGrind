class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = -1 
        res = collections.deque([])
        
        if not heights: return []

        for i in reversed(range(len(heights))):
            currHeight = heights[i]
            if currHeight > maxHeight: 
                res.appendleft(i)
                maxHeight = currHeight
        return res