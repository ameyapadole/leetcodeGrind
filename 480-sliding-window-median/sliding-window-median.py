import heapq
from collections import defaultdict
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        hash_table = defaultdict(int)
        lo = []  # max heap (simulated by pushing negative values)
        hi = []  # min heap
        
        i = 0  # index of current incoming element being processed

        # Initialize the heaps
        while i < k:
            heapq.heappush(lo, -nums[i])
            i += 1

        for _ in range(k // 2):
            heapq.heappush(hi, -heapq.heappop(lo))

        while True:
            # Get median of the current window
            if k % 2 == 1:
                medians.append(-lo[0])  # top of lo is the max element
            else:
                medians.append((-lo[0] + hi[0]) * 0.5)  # median for even window

            if i >= len(nums):
                break  # Break if all elements are processed

            out_num = nums[i - k]  # outgoing element
            in_num = nums[i]  # incoming element
            i += 1
            balance = 0  # balance factor

            # Remove the outgoing element from the current window
            if out_num <= -lo[0]:
                balance -= 1
            else:
                balance += 1
            hash_table[out_num] += 1

            # Add the incoming element into the window
            if in_num <= -lo[0]:
                balance += 1
                heapq.heappush(lo, -in_num)
            else:
                balance -= 1
                heapq.heappush(hi, in_num)

            # Re-balance heaps
            if balance < 0:  # lo needs more valid elements
                heapq.heappush(lo, -heapq.heappop(hi))
                balance += 1
            if balance > 0:  # hi needs more valid elements
                heapq.heappush(hi, -heapq.heappop(lo))
                balance -= 1

            # Remove invalid numbers that should be discarded from heap tops
            while lo and hash_table[-lo[0]] > 0:
                hash_table[-lo[0]] -= 1
                heapq.heappop(lo)

            while hi and hash_table[hi[0]] > 0:
                hash_table[hi[0]] -= 1
                heapq.heappop(hi)

        return medians
