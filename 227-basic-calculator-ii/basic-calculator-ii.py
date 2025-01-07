class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        operator = '+'
        N = len(s)

        for i, c in enumerate(s):
            if c.isdigit():
                number = number * 10 + int(c)
            if not c.isdigit() and not c.isspace() or i == N - 1:
                if operator == '+':
                    stack.append(number)
                elif operator == '-':
                    stack.append(-number)
                elif operator == '*':
                    stack.append(stack.pop() * number)
                elif operator == '/':
                    stack.append(int(stack.pop() / number))
                operator = c
                number = 0
        return sum(stack)
