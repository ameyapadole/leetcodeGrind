class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        operation = "+"
        num = 0 

        if not s:
            return 0
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            
            if not c.isdigit() and not c.isspace() or i == n - 1:
                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == "*":
                    stack.append(stack.pop() * num)
                elif operation == "/":
                    stack.append(int(stack.pop() / num))
                operation = c
                num = 0
        return sum(stack)
        