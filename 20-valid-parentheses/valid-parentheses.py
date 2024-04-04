class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping:
                topelement = stack.pop() if stack else '#'

                if mapping[char] != topelement:
                    return False
            else:
                stack.append(char)
        
        return not stack
        
        #Time = O(n)
        #Space = O(n)
        