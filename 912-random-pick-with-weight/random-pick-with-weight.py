class Solution:

    def __init__(self, w: List[int]):
        self.prefixsums = []
        prefixsum = 0 
        for weight in w:
            prefixsum += weight
            self.prefixsums.append(prefixsum)
        self.total = prefixsum
        
    def pickIndex(self) -> int:
        
        target = self.total * random.random()
        l = 0 
        r = len(self.prefixsums) - 1
        while l < r:
            m = (l + r) // 2
            if target > self.prefixsums[m]:
                l = m + 1
            else:
                r = m 
        return l 


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()