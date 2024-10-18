class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {")":"(", "}":"{", "]":"["}

        for char in s: 
            if char in hashmap: 
                topElement = stack.pop() if stack else '#'

                if topElement != hashmap[char]:
                    return False
            else:
                stack.append(char)
        return not stack