class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        counter = collections.Counter(nums)

        for num in nums:
            if counter[num] > len(nums) // 2:
                return num