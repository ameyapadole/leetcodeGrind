class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [nums[0]]
        running = nums[0]
        for i in range(1, len(nums)):
            running += nums[i]
            res.append(running)
        return res
        