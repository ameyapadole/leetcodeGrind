class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        prefixSum = 0 
        for weight in w:
            prefixSum += weight
            self.prefixSums.append(prefixSum)
        self.total = prefixSum
        

    def pickIndex(self) -> int:
        target = self.total * random.random()
        l = 0 
        r = len(self.prefixSums)
        while l < r:
            m = (l + r) // 2
            if target > self.prefixSums[m]:
                l = m + 1
            else:
                r = m 
        return l
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()