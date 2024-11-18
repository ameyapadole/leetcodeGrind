class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        current_number = 0
        last_number = 0
        result = 0
        operation = '+'
        
        for i, current_char in enumerate(s):
            if current_char.isdigit():
                current_number = (current_number * 10) + int(current_char)
            
            if (not current_char.isdigit() and not current_char.isspace()) or i == len(s) - 1:
                if operation == '+':
                    result += last_number
                    last_number = current_number
                elif operation == '-':
                    result += last_number
                    last_number = -current_number
                elif operation == '*':
                    last_number = last_number * current_number
                elif operation == '/':
                    last_number = int(last_number / current_number)  # Integer division
                
                operation = current_char
                current_number = 0
        
        result += last_number
        return result
