class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current_sum = sum(nums[:k])
        # Initialize the result with the first sum
        max_sum = current_sum
        
        # Iterate over the remaining elements, updating the sliding window sum
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / k