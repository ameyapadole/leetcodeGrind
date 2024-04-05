class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        l = 0 
        r = len(nums) - 1
        res = [0] * length
        
        for i in range(length - 1, -1, -1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
            res[i] = square * square
        return res
