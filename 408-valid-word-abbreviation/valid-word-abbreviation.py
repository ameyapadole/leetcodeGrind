class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 
        j = 0 
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False 
                num_start = j 
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                number = int(abbr[num_start:j])
                i += number
            
            else:
                if i >= len(word) or word[i] != abbr[j]:
                    return False 

                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
                
        