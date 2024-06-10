class Solution:
    def pivotInteger(self, n: int) -> int:
        l = 1 
        r = n 

        totalsum = n * (n + 1) // 2

        while l < r:
            mid = (l + r) // 2

            if mid * mid - totalsum < 0: 
                l = mid + 1
            else:
                r = mid 
        
        if l * l - totalsum == 0:
            return l
        
        else:
            return -1
        

        