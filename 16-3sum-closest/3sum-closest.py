class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                targetSum = nums[i] + nums[l] + nums[r]
                if abs(targetSum - target) < abs(diff):
                    diff = target - targetSum
                if targetSum < target:
                    l += 1
                else: 
                    r -= 1
            if diff == 0:
                break
        return target - diff        