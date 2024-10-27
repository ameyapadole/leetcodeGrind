class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        right_max = [0] * len(nums)
        i = len(nums) - 1
        prev_max = 0

        for n in reversed(nums):
            right_max[i] = max(prev_max, n)
            prev_max = right_max[i]
            i -= 1
        res = 0
        l = 0 
        for r in range(len(nums)):
            while nums[l] > right_max[r]:
                l += 1
            res = max(res, r - l)
        return res
    
        