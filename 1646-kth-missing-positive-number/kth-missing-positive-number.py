class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0 
        r = len(arr) - 1
        
        while l <= r: 
            m = (l + r) // 2
            if arr[m] - m - 1 < k:
                l = m + 1
            else:
                r = m - 1
        return l + k 