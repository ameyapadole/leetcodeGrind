class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if detail[11:13] > "60":
                count += 1            
            else:
                continue
        return count