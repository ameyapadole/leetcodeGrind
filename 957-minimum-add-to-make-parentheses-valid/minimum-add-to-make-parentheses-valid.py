class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        minadd = 0

        for char in s:
            if char == "(":
                stack.append(char)
            elif char == ")":
                if stack: 
                    stack.pop()
                else:
                    minadd += 1
        return minadd + len(stack)