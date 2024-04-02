class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
        
        #Time = O(n) since we do search() and insert() for n times and each operation take constant time
        #Space = O(n) since we use a hashset
