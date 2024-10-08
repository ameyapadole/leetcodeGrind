class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res = []
        a, b, c = 0, 0, 0

        while a < len(arr1) and b < len(arr2) and c < len(arr3):
            if arr1[a] == arr2[b] == arr3[c]:
                res.append(arr1[a])
                a += 1
                b += 1
                c += 1
            else:
                if arr1[a] < arr2[b]:
                    a += 1
                elif arr2[b] < arr3[c]:
                    b += 1
                else:
                    c += 1
        return res

        