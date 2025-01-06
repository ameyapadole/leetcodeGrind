class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0 
        res = 0 
        prefix = { 0: 1 }

        for n in nums: 
            currSum += n
            diff = currSum - k 
            res += prefix.get(diff, 0)
            prefix[currSum] = 1 + prefix.get(currSum, 0)
        return res