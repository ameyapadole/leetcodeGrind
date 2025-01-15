class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        char_map = {}

        # Build the hashmap with character counts
        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1

        # Iterate through the string again to find the first repeating character
        for index, char in enumerate(s):
            if char_map[char] == 1:
                return index  # Return the index of the first repeated character
        return -1 