class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lenS = len(s)
        lenP = len(p)
        
        dp = [[False] * (lenP + 1) for _ in range(lenS + 1)]

        dp[0][0] = True

        for i in range(1, lenP + 1):
            if p[i -1] == "*":
                dp[0][i] = dp[0][i - 1]
        
        for i in range(1, lenS + 1):
            for j in range(1, lenP + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i -1][j-1]
                
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i -1][j] or dp[i][j-1]
        
        return dp[lenS][lenP]
