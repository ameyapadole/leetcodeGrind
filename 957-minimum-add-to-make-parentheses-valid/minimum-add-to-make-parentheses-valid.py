class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openBrackets = 0
        minAdds = 0 
        for c in s: 
            if c == "(":
                openBrackets += 1
            else:
                if openBrackets > 0:
                    openBrackets -= 1
                else:
                    minAdds += 1
        return minAdds + openBrackets

        