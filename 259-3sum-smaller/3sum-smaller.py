class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
