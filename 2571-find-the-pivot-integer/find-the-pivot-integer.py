class Solution:
    def pivotInteger(self, n: int) -> int:
        l = 1 
        r = n 
        leftsum = 1
        rightsum = n 

        if n == 1:
            return n 

        while l < r:
            if leftsum < rightsum:
                leftsum += l + 1
                l += 1
            else:
                rightsum += r - 1
                r -= 1

            if leftsum == rightsum and l + 1 == r - 1:
                return l + 1
        
        return -1 


        