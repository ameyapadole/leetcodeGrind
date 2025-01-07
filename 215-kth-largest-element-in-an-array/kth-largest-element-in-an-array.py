class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, k):
            pivot = random.choice(nums)
            l, m, r = [], [], []
            for num in nums:
                if num > pivot:
                    l.append(num)
                elif num < pivot:
                    r.append(num)
                else:
                    m.append(num)
            if len(l) >= k:
                return quickselect(l, k)
            if len(l) + len(m) < k:
                return quickselect(r, k - len(l) - len(m))
            return pivot
        return quickselect(nums, k)
        