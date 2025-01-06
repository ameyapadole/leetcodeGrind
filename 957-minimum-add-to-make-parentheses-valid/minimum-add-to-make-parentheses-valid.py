class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openbrackets = 0
        minadd = 0 

        for char in s: 
            if char == '(':
                openbrackets += 1
            else:
                if openbrackets > 0:
                    openbrackets -= 1
                else:
                    minadd += 1
        return minadd + openbrackets 