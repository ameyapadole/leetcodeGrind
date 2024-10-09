class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        n = len(s) - 1
        for i in range(n):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
