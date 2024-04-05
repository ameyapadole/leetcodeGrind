class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0 
        r = len(nums) - 1

        for i in range(len(nums)- 1, -1, - 1):
            if abs(nums[l]) < abs(nums[r]):
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
            res[i] = square * square
        return res
        #Time = O(n)
        #Space = O(n)