class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        result = 0 
        prefixSum = {0 : 1}
        # t = O(n)
        # s = O(n)

        for n in nums:
            currSum += n
            diff = currSum - k 

            result += prefixSum.get(diff,0)
            prefixSum[currSum] = 1 +  prefixSum.get(currSum,0)
        
        return result