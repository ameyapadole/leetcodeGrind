class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0 
        r = len(nums)
        while l < r: 
            if nums[l] == val: 
                nums[l] = nums[r - 1] 
                #Swap Current Element with the last element.
                r -= 1
            else:
                l += 1
        return r

        """
        Time complexity : O(n).
        
        Both l and r traverse at most r steps. 
        In this approach, the number of assignment operations is equal to the number of elements to remove. 
        So it is more efficient if elements to remove are rare.

        Space complexity : O(1).
        """