import random

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def quickselect(points, k):
            pivot = random.choice(points)
            pivot_dist = pivot[0] ** 2 + pivot[1] ** 2  # Calculate squared distance of pivot
            l, m, r = [], [], []

            # Partition points into three groups
            for point in points:
                dist = point[0] ** 2 + point[1] ** 2  # Calculate squared distance
                if dist < pivot_dist:
                    l.append(point)  # Points closer than the pivot
                elif dist > pivot_dist:
                    r.append(point)  # Points farther than the pivot
                else:
                    m.append(point)  # Points equal to the pivot distance

            # Determine where k falls
            if len(l) >= k:
                return quickselect(l, k)  # k closest points are in `l`
            elif len(l) + len(m) < k:
                # Include points from `r`
                return l + m + quickselect(r, k - len(l) - len(m))
            else:
                # The k closest points are in `l + m`
                return l + m

        return quickselect(points, k)
