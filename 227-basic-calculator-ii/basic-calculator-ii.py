class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0 
        operator = "+"
        n = len(s)

        for i, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)

            if not char.isdigit() and not char.isspace() or i == n -1:

                if operator == "+":
                    stack.append(number)
                
                elif operator == "-":
                    stack.append(-number)

                elif operator == "*":
                    stack.append(stack.pop() * number)
                
                elif operator == "/":
                    stack.append(int(stack.pop() / number))
                operator = char
                number = 0 

        return sum(stack)

        