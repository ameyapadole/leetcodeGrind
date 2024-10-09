class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0 
        for passenger in details:
            age = int(passenger[11:13])

            if age > 60:
                res += 1
        return res

        