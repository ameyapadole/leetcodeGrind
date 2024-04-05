class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = collections.Counter(nums)
        for num in nums:
            if count[num] > (len(nums))//2:
                return num
        

        