class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickselect(nums, k):
            l, m, r = [], [], []
            pivot = random.choice(nums)

            for num in nums:
                if num > pivot:
                    l.append(num)
                elif num < pivot:
                    r.append(num)
                else:
                    m.append(num)
            if k <= len(l):
                return quickselect(l, k)
            if k > len(l) + len(m):
                return quickselect(r, k - len(l) - len(m))
            return pivot
        return quickselect(nums, k)