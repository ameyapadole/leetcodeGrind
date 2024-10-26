class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i, num in enumerate(nums):
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                targetSum = num + nums[l] + nums[r]
                if abs(target - targetSum) < abs(diff):
                    diff = target - targetSum 
                if targetSum < target:
                    l += 1
                else:
                    r -= 1
            if diff == 0:
                break
        return target - diff 
        