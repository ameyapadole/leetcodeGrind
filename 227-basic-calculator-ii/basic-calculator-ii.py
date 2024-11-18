class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n = len(s)
        operator = '+'
        number = 0
        for i, c in enumerate(s):
            if c.isdigit():
                number = number * 10 + int(c)
            if not c.isdigit() and not c.isspace() or i == n - 1:
                if operator == '+': 
                    stack.append(number)

                elif operator == '-':
                    stack.append(-number)
                elif operator == '/':
                    stack.append(int(stack.pop()/ number))
                elif operator == '*':
                    stack.append(stack.pop() * number)
                operator = c 
                number = 0        
        return sum(stack)
        