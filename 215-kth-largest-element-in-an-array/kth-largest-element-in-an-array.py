class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            pivot = random.choice(nums)
            l, m, r = [], [], []

            for num in nums:
                if num > pivot:
                    l.append(num)
                elif num < pivot:
                    r.append(num)
                else:
                    m.append(num)
            
            if k <= len(l):
                return quickSelect(l, k)
            
            if len(l) + len(m) < k:
                return quickSelect(r, k - len(l) - len(m))

            return pivot
        return quickSelect(nums, k)        