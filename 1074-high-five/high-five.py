class Solution:    
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
            K = 5
            all_scores = defaultdict(list)

            # Collect scores for each ID using a max-heap
            for id, score in items:
                heapq.heappush(all_scores[id], -score)

            solution = []
            for id, scores in sorted(all_scores.items()):
                # Obtain the top K scores and calculate their average
                sum_top_k = -sum(heapq.heappop(scores) for _ in range(K))
                solution.append([id, sum_top_k // K])

            return solution