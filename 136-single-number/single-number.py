class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1

        for num in seen:
            if seen[num] == 1:
                return num
        