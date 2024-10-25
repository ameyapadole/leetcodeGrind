class Solution:
    def reorganizeString(self, s: str) -> str:

        length = len(s)
        charCount = Counter(s)
        maxFreq = max(charCount.values())

        if maxFreq > (length + 1) // 2:
            return ""
        
        index = 0
        res = [None] * length

        for char, freq in charCount.most_common():
            while freq:
                res[index] = char
                freq -= 1
                index += 2
                if index >= length:
                    index = 1
        return "".join(res)

        