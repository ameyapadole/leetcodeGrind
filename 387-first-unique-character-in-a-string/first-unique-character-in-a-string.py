class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}

        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1
        
        for index, char in enumerate(s):
            if charMap[char] == 1:
                return index
        
        return -1
            
        