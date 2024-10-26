class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [[-num, char] for char, num in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        res = ""
        while prev or maxHeap:
            if prev and not maxHeap:
                return ""
            
            num, char  = heapq.heappop(maxHeap)
            res += char
            num += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if num != 0:
                prev = [num, char]
        
        return res