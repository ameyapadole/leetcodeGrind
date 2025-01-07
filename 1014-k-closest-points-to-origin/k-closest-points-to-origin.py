import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def quickselect(points, k):
            pivot = random.choice(points)
            pivot_dist = squared_distance(pivot)
            closer, equal, farther = [], [], []

            # Partition points into three groups
            for point in points:
                dist = squared_distance(point)
                if dist < pivot_dist:
                    closer.append(point)
                elif dist > pivot_dist:
                    farther.append(point)
                else:
                    equal.append(point)

            # Determine where k falls
            if len(closer) >= k:
                return quickselect(closer, k)  # k closest points are in `closer`
            elif len(closer) + len(equal) < k:
                # Need to include points from `farther`
                return closer + equal + quickselect(farther, k - len(closer) - len(equal))
            else:
                # The k closest points are in `closer + equal`
                return closer + equal

        def squared_distance(point):
            return point[0] ** 2 + point[1] ** 2

        return quickselect(points, k)
