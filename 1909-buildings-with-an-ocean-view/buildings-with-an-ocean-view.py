class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        maxHeight = -1 
        res = []

        for i in reversed(range(len(heights))):
            if maxHeight < heights[i]:
                res.append(i)
                maxHeight = heights[i]
        res.reverse()
        return res