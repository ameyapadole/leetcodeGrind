class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        l = self.sortArray(nums[:mid])
        r = self.sortArray(nums[mid:])
        return self.mergesort(l, r)

    def mergesort(self, left, right):
        i, j = 0, 0 
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])

        return res


    